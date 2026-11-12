"""QR asset checks; optional ZXing checks decode the actual image, not metadata."""
from io import BytesIO
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

try:
    from PIL import Image, ImageEnhance
    import zxingcpp
except ImportError:
    Image = zxingcpp = None


ROOT = Path(__file__).resolve().parents[1]
URL = "https://shaokun91.github.io/darwin-agent-website/"


class QRAssetTests(unittest.TestCase):
    def test_svg_is_self_contained_and_has_quiet_zone(self):
        root = ET.parse(ROOT / "assets/darwin-agent-qr-da.svg").getroot()
        ns = {"svg": "http://www.w3.org/2000/svg"}
        self.assertEqual(root.attrib["viewBox"], "0 0 49 49")
        self.assertIn(URL, root.find("svg:desc", ns).text)
        embedded = root.find("svg:image", ns)
        self.assertTrue(embedded.attrib["href"].startswith("data:image/png;base64,"))
        self.assertEqual(root.find("svg:rect", ns).attrib["fill"], "#fff")
        self.assertTrue((ROOT / "assets/darwin-mark-da-orange.png").is_file())
        # Data modules must stay inside the four-module white border.
        import re
        cells = re.findall(r"M(\d+) (\d+)h1v1h-1z", root.find("svg:path", ns).attrib["d"])
        self.assertGreater(len(cells), 500)
        self.assertTrue(all(4 <= int(x) < 45 and 4 <= int(y) < 45 for x, y in cells))


@unittest.skipUnless(Image and zxingcpp, "Install Pillow and zxing-cpp to decode QR images")
class QRDecodeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.image = Image.open(ROOT / "assets/darwin-agent-qr-da.png").convert("RGB")

    def assertDecodes(self, image):
        result = zxingcpp.read_barcode(image)
        self.assertIsNotNone(result, "No QR code decoded")
        self.assertEqual(result.text, URL)

    def test_original_and_resized_images(self):
        self.assertEqual(self.image.size, (1176, 1176))
        for size in [1176, 490, 245, 196, 147]:
            with self.subTest(size=size):
                self.assertDecodes(self.image.resize((size, size), Image.Resampling.LANCZOS))

    def test_rotation_compression_and_grayscale(self):
        small = self.image.resize((245, 245), Image.Resampling.LANCZOS)
        for angle in [-15, 15, 45, 90]:
            with self.subTest(angle=angle):
                self.assertDecodes(small.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True, fillcolor="white"))
        self.assertDecodes(small.convert("L"))
        self.assertDecodes(ImageEnhance.Contrast(small).enhance(0.65))
        jpeg = BytesIO()
        small.save(jpeg, format="JPEG", quality=55)
        jpeg.seek(0)
        self.assertDecodes(Image.open(jpeg))

    def test_lettermark_uses_xiaomi_orange(self):
        with Image.open(ROOT / "assets/darwin-mark-da-orange.png") as mark:
            self.assertEqual(mark.mode, "RGBA")
            self.assertEqual(mark.getpixel((0, 0))[3], 0)
            orange_pixels = sum(count for count, color in mark.getcolors(mark.width * mark.height)
                                if color == (255, 105, 0, 255))
            self.assertGreater(orange_pixels, 10000)


if __name__ == "__main__":
    unittest.main()

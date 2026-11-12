"""Build the static homepage QR assets. No QR service or browser library needed.

Development dependencies: qrcode==8.2 and Pillow.
Decode tests (optional): zxing-cpp==2.3.0.
"""
from base64 import b64encode
from io import BytesIO
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw
import qrcode
from qrcode.constants import ERROR_CORRECT_H


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
URL = "https://shaokun91.github.io/darwin-agent-website/"
INK = "#151714"
BORDER = 4
BOX_SIZE = 24
PLATE_MODULES = 9
LOGO_MODULES = 8


def build():
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=BOX_SIZE, border=BORDER)
    qr.add_data(URL, optimize=0)
    qr.make(fit=True)
    # This URL fits version 6 (41 data modules). Keep the logo clear of all
    # finder, timing, and alignment patterns; fail rather than silently resize
    # into a different QR layout if the destination changes in the future.
    if qr.version != 6:
        raise ValueError(f"Review logo placement for QR version {qr.version}")
    matrix = qr.get_matrix()
    extent = len(matrix)
    pixels = extent * BOX_SIZE
    plate_start = (extent - PLATE_MODULES) // 2
    plate_end = plate_start + PLATE_MODULES
    logo_start = (extent - LOGO_MODULES) / 2
    image = Image.new("RGB", (pixels, pixels), "white")
    draw = ImageDraw.Draw(image)
    cells = []
    for y, row in enumerate(matrix):
        for x, active in enumerate(row):
            if active:
                draw.rectangle((x * BOX_SIZE, y * BOX_SIZE,
                                (x + 1) * BOX_SIZE - 1, (y + 1) * BOX_SIZE - 1), fill=INK)
                cells.append(f"M{x} {y}h1v1h-1z")
    draw.rectangle((plate_start * BOX_SIZE, plate_start * BOX_SIZE,
                    plate_end * BOX_SIZE - 1, plate_end * BOX_SIZE - 1), fill="white")
    logo = Image.open(ASSETS / "darwin-mark-orange.png").convert("RGB")
    logo_pixels = LOGO_MODULES * BOX_SIZE
    image.paste(logo.resize((logo_pixels, logo_pixels), Image.Resampling.LANCZOS),
                (round(logo_start * BOX_SIZE), round(logo_start * BOX_SIZE)))
    image.save(ASSETS / "darwin-agent-qr.png", optimize=True)

    # Embed the normalized logo, so the downloaded SVG is fully self-contained.
    encoded = BytesIO()
    logo.save(encoded, format="PNG", optimize=True)
    data_url = "data:image/png;base64," + b64encode(encoded.getvalue()).decode("ascii")
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{pixels}" height="{pixels}" viewBox="0 0 {extent} {extent}" role="img" aria-labelledby="qr-title qr-description">
  <title id="qr-title">Darwin Agent homepage QR code</title>
  <desc id="qr-description">High-error-correction QR code for {escape(URL)} with an orange Darwin D lettermark.</desc>
  <rect width="{extent}" height="{extent}" fill="#fff"/>
  <path d="{"".join(cells)}" fill="{INK}" shape-rendering="crispEdges"/>
  <rect x="{plate_start}" y="{plate_start}" width="{PLATE_MODULES}" height="{PLATE_MODULES}" fill="#fff"/>
  <image x="{logo_start}" y="{logo_start}" width="{LOGO_MODULES}" height="{LOGO_MODULES}" href="{data_url}"/>
</svg>
'''
    (ASSETS / "darwin-agent-qr.svg").write_text(svg, encoding="utf-8")
    print(f"QR v{qr.version}, H correction, {extent} modules including quiet zone, {pixels}px PNG")
    print(URL)


if __name__ == "__main__":
    build()

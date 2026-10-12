"""Generate deterministic print artwork; never used by the website at runtime.

Install qrcode==8.2 pillow==12.3.0 opencv-python-headless==5.0.0.93 cairosvg==2.9.1
in a temporary virtual environment, then run this script from any directory.
Only run after the permanent live address has been verified.
"""
from pathlib import Path
import xml.etree.ElementTree as ET

import cairosvg
import cv2
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image

URL = "https://mjfsch.github.io/"
OUTPUT = Path(__file__).resolve().parents[1] / "qr"


def main():
    OUTPUT.mkdir(exist_ok=True)
    code = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=64, border=4)
    code.add_data(URL)
    code.make(fit=True)
    matrix = code.get_matrix()
    side = len(matrix)
    # An opaque white background preserves the quiet zone on black garments.
    svg = ET.Element("svg", {"xmlns": "http://www.w3.org/2000/svg", "width": "45mm", "height": "45mm", "viewBox": f"0 0 {side} {side}", "shape-rendering": "crispEdges"})
    ET.SubElement(svg, "title").text = "Permanent landing page: " + URL
    ET.SubElement(svg, "rect", {"width": str(side), "height": str(side), "fill": "#fff"})
    path = " ".join(f"M{x},{y}h1v1h-1z" for y, row in enumerate(matrix) for x, dark in enumerate(row) if dark)
    ET.SubElement(svg, "path", {"d": path, "fill": "#000"})
    svg_path = OUTPUT / "mjfsch-sleeve.svg"
    ET.ElementTree(svg).write(svg_path, encoding="utf-8", xml_declaration=True)
    png_path = OUTPUT / "mjfsch-sleeve.png"
    code.make_image(fill_color="black", back_color="white").convert("RGB").save(png_path, dpi=(1200, 1200))
    # Independently decode the actual PNG and rasterized SVG, not generator data.
    detector = cv2.QRCodeDetector()
    decoded_png = detector.detectAndDecode(cv2.imread(str(png_path)))[0]
    raster = cairosvg.svg2png(url=str(svg_path), output_width=1184, output_height=1184)
    import numpy as np
    decoded_svg = detector.detectAndDecode(cv2.imdecode(np.frombuffer(raster, dtype=np.uint8), cv2.IMREAD_COLOR))[0]
    assert decoded_png == URL, repr(decoded_png)
    assert decoded_svg == URL, repr(decoded_svg)
    for name in (svg_path.name, png_path.name):
        print(f"Verified {name}: {URL}")
    # Check exact four-module quiet zone and PNG corner/background opacity.
    assert not any(any(row) for row in matrix[:4] + matrix[-4:])
    assert not any(any(row[:4] + row[-4:]) for row in matrix)
    with Image.open(png_path) as image:
        assert image.mode == "RGB" and image.getpixel((0, 0)) == (255, 255, 255)
        print(f"Version {code.version}, H correction, {code.modules_count} modules + 4-module quiet zone, PNG {image.width} x {image.height}")


if __name__ == "__main__":
    main()

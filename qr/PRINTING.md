# Sleeve QR printing

Encoded destination: **https://mjfsch.github.io/**. This is the permanent landing
page, never an invite, event link or tracking redirect.

## Artwork

- `mjfsch-sleeve.svg`: preferred for printing; sharp at any size, supplied at
  **45 x 45 mm**, with an opaque white background and black square modules.
- `mjfsch-sleeve.png`: **2624 x 2624 px** RGB PNG, the same code with an opaque white
  background. Set its physical print size to **45 x 45 mm** (or larger) in the
  print layout; don't rely on the application's automatic DPI sizing.
- Both files include a **four-module white quiet zone on every side**. Keep the
  entire white square; never crop the margins or remove the white background.
- Error correction: **H**. No logo overlays, decorative shapes or rounded modules.

This is a version-4 symbol: 33 x 33 modules, or 41 x 41 including the margins.
At 45 mm overall, each module is about 1.10 mm and each quiet margin is 4.39 mm.
At the 35 mm practical minimum, each module is about 0.85 mm.

## Size and contrast on a black T-shirt

Our practical recommendation for an exhibition sleeve is **45-50 mm square**,
including the white quiet zone. Treat **35 mm square** as the practical minimum
for this artwork, subject to a successful test on the actual printed garment.
This is a garment-print recommendation, not a guarantee or universal QR minimum:
ink spread, fabric texture, folds and viewing distance affect scanning.

Print **black modules on a solid opaque white square**. On black fabric, ask the
printer for a white underbase/block so black fabric cannot show through the white
modules or quiet zone. Don't invert the code to white modules on black fabric.
Keep text, stitching, seams, logos and sleeve edges outside the white margin.
Use a smooth, relatively flat sleeve area and preserve the square proportions.
Avoid embroidery, metallic/glitter inks and stretched/distorted artwork.

Before printing the full batch, scan a physical 45 mm proof with at least two
phones, then scan the sample shirt while worn, in indoor lighting, at roughly
20-40 cm. Test gentle curvature and a slight angle. Check the browser opens the
exact live address. Test again after washing a sample. If scanning is hesitant,
increase to 50 mm or move the print to a flatter area.

The four-module margin follows [DENSO WAVE's QR guidance](https://www.qrcode.com/en/howto/code.html).
H correction provides resilience to damage; it does not make cropping or
distortion safe. See [DENSO WAVE on error correction](https://www.qrcode.com/en/about/error_correction.html).

## Regeneration

No website build is required. The optional `tools/generate_qr.py` uses the standard
`qrcode` encoder and independently decodes the PNG and a rasterized SVG with
OpenCV. Its dependency versions are documented in the script. Run it only after
verifying the permanent URL is live; it prints the decoded URL, pixel size and
symbol dimensions. Link/event updates never require regeneration.

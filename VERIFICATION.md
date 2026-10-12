# Verification record

Date: 12 October 2026. The existing public `mjfsch.github.io` repository was
verified empty via GitHub's Contents API before cloning; the previous root URL
returned 404 and Pages was not configured. No existing files were overwritten.
The unrelated CoPrintHelperBot working tree was not edited.

## Browser and accessibility checks

Automated real Chromium checks with Playwright and axe-core 4.10.3:

- Viewports: 280x653, 320x568, 360x800, 375x812, 390x844, 430x932,
  768x1024 and 1440x900. No horizontal overflow, blank links or dead controls.
- axe WCAG 2 A/AA, WCAG 2.1 AA and best-practice rules: zero violations at
  every viewport, including automated text contrast and accessible-name checks.
- Mobile touch emulation at 390x844 and device pixel ratio 3.
- Text enlarged to 200% at 320px; 320px also checks the reflow width of a
  1280px desktop at 400% zoom. Content remains readable without sideways scroll.
- Visible keyboard focus, sequential Tab order, Enter activation, and every
  interactive target at least 44px high. Logical headings, named navigation,
  decorative SVGs hidden from assistive technology, polite clipboard live region.
- Clipboard success copies exactly `mjfsch`, confirms it, and resets its label.
  Clipboard permission failure/unavailable API selects the visible handle and
  gives manual instructions. Content and links also work with JavaScript disabled.
- Forced-colour mode and reduced-motion preference. No animation is shipped.
- No JavaScript errors, third-party runtime requests or cookies. Four small
  static assets (HTML, CSS, JS, favicon) total approximately 12 KB uncompressed.
- Mobile and desktop full-page screenshots were visually inspected.
- `node --check script.js` and `git diff --check` passed.

Automated checks and semantic inspection do not replace a hands-on assistive
technology session. Physical iOS/Android devices and actual screen-reader speech
were not available in this environment.

## Destination checks

- CoPrint homepage and GitHub profile return HTTP 200.
- Community invite verified with Discord's invite API: correct "Co Print Official"
  server, welcome channel and no expiry. Source: https://coprint3d.com/.
- Quadro Kickstarter URL matches CoPrint's homepage destination and resolves in
  web lookup. Direct automated requests receive Kickstarter's HTTP 403 bot
  protection; normal visitor interaction with Kickstarter could not be automated.
- No guessed personal Discord URL and no placeholder or broken scheduled-event
  button. The unconfirmed event remains a text status.

## Deployment and QR

The deployment and decoded QR verification are recorded here after publication.
The print guide includes a physical proof test because software decoding cannot
verify ink, fabric, sleeve curvature or the printed garment.

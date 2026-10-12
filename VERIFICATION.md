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
  static assets (HTML, CSS, JS, favicon) total approximately 11 KB uncompressed.
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
- Personal Discord profile: the owner supplied
  `https://discord.com/users/237471776957792257`; no user ID was guessed.
  The URL returns HTTP 200; Discord may require sign-in to display the profile.
- YouTube returns HTTP 200 with title `mjfsch - YouTube` and canonical handle
  `/@mjfsch`. TikTok returns HTTP 200 with `uniqueId: mjfsch`, `nickname: mjfsch`
  and a successful (`0`) profile status code in its page data.
- YouTube and TikTok appear below the community invite. Social links share
  one row to keep the page compact. The copy button is a small secondary control
  with a 44px tap target; the direct Discord profile is the primary contact link.
- The livestream/event section was removed at the owner's request, including
  event status and metadata references. No placeholder scheduled-event links.

## Deployment and QR

- Confirmed live URL: **https://mjfsch.github.io/**, HTTP 200 over HTTPS.
  GitHub Pages reports `built`, no build error, source `main` at `/`, legacy
  branch publishing and `https_enforced: true`. No custom workflow was added.
- Live browser checks passed: content and all runtime assets match the local
  source byte for byte, correct canonical URL, mobile layout, zero axe violations,
  actual HTTPS clipboard read/write and successful community-link navigation to
  `https://discord.com/invite/rPAMgVsdjP`. No cookies or third-party runtime requests.
- Generated QR artwork only after the live URL had been confirmed. OpenCV's
  independent decoder read the actual PNG and the actual SVG rasterized with
  CairoSVG; both returned exactly `https://mjfsch.github.io/`.
- QR version 4, error correction H, 33x33 symbol modules, four white modules on
  all sides, 41x41 total grid. SVG physical size 45x45 mm; PNG 2624x2624 px, RGB
  with a white background. Quiet margins and background opacity were asserted.
- Physical garment scanning still requires a proof; software cannot verify ink,
  fabric, sleeve curvature or the actual printed garment. See `qr/PRINTING.md`.

## Subsequent content update

- 12 October 2026: the email contact link was removed from the published page,
  and the volunteer wording was made friendlier. The earlier browser test results
  above describe the previous revision; they were not rerun for this text-only update.

## Logo and text cleanup

- Synced the owner's intervening changes before editing. Preserved the compact
  copy control beside the username and the removal of the public email address.
- Platform logos now have explicit colours in the local SVG sprite: Discord
  blurple, YouTube red/white, TikTok cyan/pink/white and Kickstarter green.
  GitHub uses its white mark on the dark background. Icon widths are 16px for
  Discord, 14px for social links and 12px for GitHub.
- Added CoPrint's original colour wordmark from its own homepage, stored locally
  and displayed at 96px wide. Removed the decorative substitute from the links.
- Removed the requested fellow-maker, volunteer and acknowledgement text, plus
  the Discord profile/community subtitles.
- Chromium checks passed at 280, 320, 390, 768 and 1440px: actual SVG rendering,
  bounded logo sizes, loaded CoPrint image, no horizontal overflow, 44px-or-larger
  interaction targets, and zero axe WCAG A/AA or best-practice violations.
- Verified actual screenshot pixels for YouTube red and both TikTok accent
  colours. Visually inspected mobile and desktop screenshots. Keyboard activation,
  clipboard copying and 200% text enlargement also passed with no failed assets
  or JavaScript errors.
- All six runtime assets remain local and total about 28 KB uncompressed.

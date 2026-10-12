# @mjfsch - CoPrint Community Ambassador

A small personal digital business card for a volunteer attending Formnext 2026.
Plain HTML/CSS and one clipboard enhancement. No build step, runtime packages,
tracking, cookies, frameworks or backend. All links and content work without JS.

Permanent address: **https://mjfsch.github.io/**

## Deploy with GitHub Pages

This repository is `mjfsch/mjfsch.github.io`. It was empty before implementation;
no existing website or files were replaced.

1. Commit the files to `main`.
2. Open [Settings > Pages](https://github.com/mjfsch/mjfsch.github.io/settings/pages).
3. Choose **Deploy from a branch**, branch **main**, folder **/(root)**, then **Save**.
4. Wait for GitHub's Pages deployment to finish, then visit the permanent address.
5. Enable **Enforce HTTPS** if it is not already enabled.

`.nojekyll` serves the static files directly. No custom Actions workflow is needed;
GitHub may show its own Pages deployment run. There is no custom domain/CNAME.
Subsequent commits to `main` publish automatically. GitHub's guide:
https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Change content and links

**`index.html` is the editable configuration location.** It contains all visible
text and destination URLs; there is no second JS configuration to keep in sync.
Use GitHub's file editor or edit locally and commit to `main`.

- Username: change the text of `id="discord-username"`, keeping its leading `@`.
  The copy button reads this value and copies it without `@`, as expected by
  Discord's Add Friend field. Update the page title/description too.
- Community invite: change the `href` immediately below `COMMUNITY INVITE`.
  Current invite: `https://discord.gg/rPAMgVsdjP`. It comes from the official
  CoPrint homepage's Discord Channel link and was verified on 12 October 2026:
  guild `1144633500922822656`, "Co Print Official", welcome channel, no expiry.
  Check a replacement opens the correct community before publishing.
- Discord profile: change the `href` under the profile URL comment. The current
  `https://discord.com/users/237471776957792257` was supplied by the page owner.
  Discord may require the visitor to sign in before showing the profile.
- YouTube, TikTok, CoPrint, Quadro Kickstarter and GitHub destinations:
  edit the matching `href` attributes. The social profiles use the owner's
  `@mjfsch` username.
  The Kickstarter destination was taken from CoPrint's own homepage.
- Colours, spacing and type: edit `style.css`. The favicon is an original abstract
  layer illustration, not an official brand logo.
- Logos: `icons.svg` stores platform vectors with explicit brand colours. CSS
  sets their sizes (16px for Discord, 14px for social links, 12px for GitHub).
  Keep those fills intact instead of applying a shared `currentColor` override.
  TikTok's colour geometry comes from
  https://github.com/gilbarbara/logos/blob/main/logos/tiktok-icon.svg, using a white
  centre on the dark background. The other platform paths come from Simple Icons.
  `coprint-logo.webp` is CoPrint's original colour wordmark from its homepage,
  displayed at 96px wide and hosted locally. Source:
  https://coprint3d.com/cdn/shop/files/cologwebp.webp?v=1738592849
  The website link uses the 14px colour mark in `coprint-mark.png`, sourced from
  CoPrint's own `apple-touch-icon.png` favicon. Both Discord links use the same
  16px icon and 10px text gap to keep their labels aligned.

## Update after Formnext

The livestream/event section was removed at the owner's request. To make the
introduction evergreen after Formnext, change "Hello from Formnext 2026!" to
"Hello, fellow maker!", remove the stand-visit paragraph and related CSS, and
refresh the description metadata. Discord, the
community links and the permanent sleeve QR stay useful without rebuilding.

## QR artwork and print guidance

See [`qr/PRINTING.md`](qr/PRINTING.md). Both QR files point only to the permanent
landing page, so invite/event updates never require a new shirt.

## Preview and verification

Run `python3 -m http.server 8765` from the repository and open
`http://localhost:8765/`. Clipboard copying works on localhost and live HTTPS.
If copying is unavailable, the page selects the visible username and explains
how to enter it manually. Without JS the button stays hidden and a manual
instruction appears.

See [`VERIFICATION.md`](VERIFICATION.md) for the tested viewports, accessibility,
clipboard, external link, QR and deployment checks. QA/QR generation tools are
development tools only; visitors download just the static page assets.

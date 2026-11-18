# Jess Zheng Media Kit Website

## Project Location
`~/Development/jesszhengg-site`

## Overview
Single-page media kit / portfolio website for content creator Jess Zheng (Bangkok-based).

## Tech Stack
- Static HTML site (single `index.html` with inline CSS/JS)
- No build step needed
- Hosted on GitHub Pages (free) with custom domain

## Hosting & Deployment
- **GitHub repo**: https://github.com/williamcoconut/jesszhengg-site
- **Branch**: `main`
- **Hosting**: GitHub Pages (free, unlimited deploys)
- **Live URL**: https://jesszheng.co
- **Fallback URL**: https://williamcoconut.github.io/jesszhengg-site/
- **Deploy workflow**: `git push` to main → GitHub Pages auto-deploys (free, no credit system)
- **Previous hosting**: Netlify (moved away due to credit limits)
- **Publish directory**: root `/`

## Project Structure
```
index.html          # The live media kit: HTML, CSS, JS (inline)
build_tiers.py      # Rebuilds the hidden tier pages from index.html. RUN AFTER EVERY index.html EDIT
enrkpf7.html        # Hidden LOW tier (generated, noindex). Never hand-edit
fkxm0t6.html        # Hidden MID tier (generated, noindex). Never hand-edit
ojk8uet.html        # Hidden HIGH tier (generated, noindex). Never hand-edit
collab/index.html   # Experimental animated rate card (see below)
collab/img/         # Resized images and clips used only by collab/
images/             # All image assets
images/logos/       # Brand/partner logos
.gitignore          # Excludes .DS_Store
```

## The /collab experiment (started 2026-08-12)
- Live at https://jesszheng.co/collab/, `noindex`, self-contained single file.
- A standalone animated rate card, separate from index.html. It is NOT a copy:
  it uses the public rates only and has its own EN/ไทย toggle, sections and
  visual language (light blush/pink theme; GSAP + ScrollTrigger from CDN).
- **index.html is the source of truth for every number.** Follower counts,
  view counts, engagement, demographics and prices must be copied from it,
  never derived. Copy each figure's qualifier too: the 1.5M and 1.09M campaign
  numbers are "IG + TikTok" combined, not single-post results.
- Do not touch index.html or the hidden tier pages (`enrkpf7.html` low,
  `ojk8uet.html` high) when working on /temp.
- `?static` in the URL freezes all animation for screenshot QC, and the page
  must stay fully readable with JS disabled and under prefers-reduced-motion.
- NOTES.md holds the full change log, the QC gotchas, and a list of "fixes"
  that were reviewed and REJECTED. Read it before changing /temp.
- Status: awaiting William's verdict (promote, iterate, or delete).

## Features
- Bilingual (English / Thai) with language toggle
- Hero section with profile info
- Collaboration showcase gallery
- Audience demographics
- Partner/brand logos
- Instagram feed integration
- Contact section (email only, phone removed)

## Key Decisions
- Phone number was removed from contact section (Feb 2026)
- **Clean premium revamp (2026-11-14)**, replacing the Jul 2026 coral/cream design
  (that one is git tag `pre-revamp-2026-11`; the one before it is `pre-redesign-backup`).
- Fonts: Trirong (display, weight 300) + Anuphan (text). Both cover Latin AND Thai,
  so EN and TH match with no separate Thai font.
- **The site stays CUTE AND PINK.** William rejected a green "premium" palette the
  same day (2026-11-14). Clean and premium is fine for layout and type; the colour
  and personality must stay pink and cute.
- Colors: blush paper #fff7f9, candy-pink panel #ffe4ec, deep berry text #4b1430,
  hot pink #d6336f (buttons, the big name, bundle + contact panels), lilac #eadffb
  behind the portrait.
- Cute details: arch portrait on a lilac arch, heart sticker, rounded image corners,
  tilted "Most popular" tag, pink dotted leaders, heart in the footer.
- Rates are a typeset price list with dotted leaders; the bundle is a hot-pink panel.
- Motion: one hero load animation, plus short muted clips of her real posts that play
  over the hero portrait and the work card covers while in view (`images/clips/`,
  `video.clip`). No scroll reveals, marquees, count-ups or tilt.
- Copy rules: no em dashes, no emoji, no all-caps labels, sentence case.
- The old "Content formats" section was folded into the rate rows (same descriptions).
- The email is selectable text plus a Copy button, because mailto does nothing in
  the Instagram/TikTok in-app browsers.
- **No prices on the public page (2026-11-18).** index.html shows "On request" (empty
  `.price` cells + CSS ::after) so Google never shows her rates. Brands get a hidden
  tier link: low enrkpf7, mid fkxm0t6 (the old public rates), high ojk8uet.
  build_tiers.py fills prices, the bundle saving (`{SAVE}`) and the USD subtitle
  (`<!--rates-sub-->` markers) and refuses to run if index.html contains a `$` price.
- Prices must keep `class="price"` and page order (IG, TikTok, FB, YT, Bundle,
  Stories, UGC, Gen Code): build_tiers.py swaps them by position.

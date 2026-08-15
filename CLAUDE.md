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
- Full visual redesign (Jul 2026): Fraunces serif + DM Sans + Noto Sans Thai (Google Fonts)
- Color scheme: coral (#e8707a), cream (#fdfaf7), dark (#141114)
- Design features: aurora gradient hero, static film-grain overlay, scroll-reveal
  animations (IntersectionObserver), count-up metrics, 3D-tilt collab cards with
  shine sweep, infinite logo marquee, tilted kinetic ticker, scroll progress bar
- All animations respect prefers-reduced-motion; grain is static (animating it
  repaints the whole page every frame and tanks performance)
- Marquees (ticker + logos) are duplicated via JS on load for seamless looping

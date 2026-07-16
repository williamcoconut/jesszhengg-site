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
index.html          # Everything: HTML, CSS, JS (inline)
images/             # All image assets
images/logos/       # Brand/partner logos
.gitignore          # Excludes .DS_Store
```

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

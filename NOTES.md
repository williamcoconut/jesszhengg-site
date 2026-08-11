# Notes

## Experimental /temp Rate Card (2026-08-12)
- Live at https://jesszheng.co/temp/ — standalone, does NOT touch index.html or tier pages
- Concept: rate card as a Bangkok night-market menu (Jess is known for street food
  content). Mains = platform rates, Sides = add-ons, Chef's Special = bundle with a
  hand-drawn neon circle that draws itself on scroll
- Uses PUBLIC rates (same as index.html), English only, noindex/nofollow meta
- Design: aubergine dark + neon pink + tungsten amber; Bricolage Grotesque display,
  Schibsted Grotesk body, Sriracha (Thai handwriting font) for menu scribbles + Thai accents
- Motion: GSAP CDN + ScrollTrigger. Char-split hero, count-up prices, scroll reveals,
  parallax glows, cursor "lantern" glow (desktop only). Page fully readable with no JS;
  prefers-reduced-motion kills all motion; `?static` query param also disables animation
  (useful for QC screenshots in the browser pane, which reloads on every capture)
- Gotcha fixed: img width/height attrs + max-width:100% stretched images until
  `height:auto` was added; profile crop needed object-position 50% 15%
- QC tip: local server via python http.server (port 8931), file:// renders as a
  static snapshot in the pane and won't scroll or animate

## Rates + Stats Update (2026-07-16)
- New rates: IG Reel $900, TikTok $900, YouTube $1,000, Bundle $1,500 (save $700);
  FB $400 and add-ons unchanged
- Follower stats refreshed from live platforms (all grown since Feb):
  TikTok 62.3K (Social Blade), IG 43.7K (verified badge), YouTube 23K, FB 20K
  → total 149K+; also added 6.4M+ TikTok likes as a metric (replaced "4 Platforms")
- Platform access notes: TikTok web bot-walls both browsers (Social Blade works as
  proxy for counts); Instagram shows profile header logged-out but blocks scrolling;
  YouTube + Facebook fully readable logged-out

## Visual Redesign (2026-07-16) — COMMITTED LOCALLY, NOT YET PUSHED
- Complete overhaul of index.html (still single-file, no build step)
- New look: editorial serif (Fraunces) + DM Sans, cream/coral palette, film grain,
  aurora gradient hero, floating stat chips, tilted ticker strip, count-up metrics,
  scroll-reveal animations, 3D-tilt collab cards, infinite partner-logo marquee
- Added: OG/meta tags for link previews, Noto Sans Thai for proper Thai rendering,
  prefers-reduced-motion support, scroll progress bar
- All content, links, rates, and EN/TH translations preserved from previous version
- Perf lesson: animating the full-page grain overlay repaints every frame — keep
  grain STATIC. Blob blur kept at 60px for GPU sanity.
- Verified in browser: desktop + mobile (375px), EN + TH, all 10 sections render
- Browser-pane quirk (dev only): screenshots capture blank when page is scrolled;
  workaround is CSS zoom or translateY at scroll 0 — not a site bug

## Hosting Migration (2026-02-16) — COMPLETE
- Moved from Netlify to GitHub Pages
- Reason: Netlify free tier hit 326/300 credits — site paused
  - 120 credits from 8 deploys (15 credits each)
  - 191.6 credits from AI inference
- GitHub Pages: free, unlimited deploys, no credit system
- Domain: jesszheng.co (registered on Porkbun)
- DNS: 4x A records + 4x AAAA records + www CNAME → GitHub Pages
- HTTPS enforced
- Had to remove/re-add custom domain to unstick SSL cert provisioning
- Live at: https://jesszheng.co
- Netlify site deactivated

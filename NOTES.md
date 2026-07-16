# Notes

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

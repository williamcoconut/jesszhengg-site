# Notes

## /temp Rate Card v5: audience proof + mobile hero (2026-08-12)
- Added an Audience section AFTER the prices (a brand manager's 2nd question,
  right where they judge whether $900 is worth it), before the brand logos:
  neon-tube bar chart of followers per platform + fact strip
- ALL numbers copied from index.html, none invented: 62.3K TikTok / 43.7K IG /
  23K YT / 20K FB (sums to the 149K+ claim), 100M+ views, 5.8% avg engagement,
  18-34, 65/35 women/men, US CA UK AU. Bar heights are honest ratios of 62.3K
  (100/70/37/32%). If these ever change, update index.html AND temp/index.html.
- Hero: added a quiet "See rates / ดูราคา" ghost button anchored to #menu
  (an action above the fold; the old review flagged time-to-price)
- Sticky bar no longer always shouts $1,500: starts "Rates from $200", swaps to
  the bundle once .special has been seen (IntersectionObserver, then disconnects)
- Mobile hero was overflowing 989px into an 844px screen with the scroll hint
  overlapping the polaroid: compact chips, smaller polaroid, hint hidden <=760px
- CSS ORDER GOTCHA: the first attempt at hiding the hint failed silently because
  the media query sat ABOVE the base .scroll-hint{display:flex} rule. Same
  specificity means source order wins. Mobile overrides must come after the base.
- Logo <img> now carry real intrinsic width/height read from the SVG/PNG files
  (guessing them would reserve the wrong space and cause the CLS being fixed)
- Corrected TikTok 62.3K -> 62K. 62.3K was derived by subtracting the other
  platforms from 149K; her media kit publishes 62K. Never state a precision she
  does not publish. All other figures verified against index.html.
- Bundle digits are now real children of the bundle timeline (were a
  fire-and-forget gsap call, which any jump or scrub would skip).

### QC gotchas in the browser pane (cost me three false diagnoses)
1. Stale cache after edits: append ?static&cb=N or you verify the OLD file.
2. When the pane is hidden/collapsed, `innerHeight` reads 0, rAF never runs
   (gsap.ticker.frame stays 0) and IntersectionObserver callbacks never fire.
   Frozen tweens then look exactly like "the trigger never fired". Check
   `document.hidden` and `gsap.ticker.frame` BEFORE concluding there is a bug.
3. `gsap.globalTimeline.totalTime(n)` suppresses callbacks, so anything inside
   a .call() appears not to run. Only tween-based state survives that jump.
4. Reading a gsap transform with /-?[\d.]+/ grabs the X value out of
   `translate(0%, -95%)` and always reports 0. Match the Y group explicitly.
   Verify the measuring tool before trusting a scary measurement.

## /temp Rate Card v4: crazier + polish (2026-08-12)
- New: velocity-reactive marquees (gsap-driven, reverse on scroll-up, timeScale
  from getVelocity; clone-to-fill kills the seam gap on wide screens; deep
  totalTime(600) so negative timeScale never hits t=0), sign drops onto chains,
  chase-light ring on bundle (::before repeating-linear-gradient, bg-position
  loop = composited; ::before so badge/stamp paint over it), ONE bundle timeline
  (roll -> circle draw -> stamp slam -> stamp recoil + sparks), parallax
  polaroids (hover moved to img filter, gsap owns polaroid transform), price
  hover pop, OG/twitter meta, scroll-hint scrub fade (scrub owns opacity solo)
- Cut by measured review (2-agent, live-browser): tuk2 (100% clipped by .book
  overflow:hidden AND same joke twice), odometer blur (unreadable prices),
  .special x-shake (price must hold still), conic sweep (generic SaaS border)
- tuk1 parks back at x:-140 after driving: parking at 108vw inflated
  document scrollWidth by 135px (body overflow-x:hidden masks it but
  programmatic scrollX could shift layout)
- Browser-pane gotcha: hidden pane pauses rAF so ScrollTriggers queue; verify
  structurally via JS, not by waiting for tweens

## /temp Rate Card v3: de-metaphored (2026-08-12)
- William: menu idea confusing; wants clear + brilliant + beautiful + CUTE
- Kept: full Bangkok atmosphere (neon sign, food/bulb doodles, tuk-tuk, polaroids,
  อร่อย! sticker now wiggling, MOST BOOKED/ยอดฮิต stamp, confetti hearts, tickers,
  odometer prices, EN/ไทย toggle) because street food IS her niche, not a metaphor
- Replaced every structural label with literal copy:
  h1 THE MENU -> RATE CARD / เรทราคา (industry phrase brands DM her with)
  Tonight's Menu -> Services & Rates / บริการ & ราคา (matches main site)
  Mains/Sides -> Content/Add-ons · คอนเทนต์/บริการเสริม
  Chef's special badge -> "3 in 1"; The Full Table -> The Bundle / แพ็คเกจรวม
  Hungry? -> Say hi! / ทักมาเลย!; house rules -> the fine print / เรื่องเล็กๆ ที่ควรรู้
  past dinner guests -> in good company / แบรนด์ดังการันตี; แม่ค้าเจส -> สวัสดีค่ะ เจสเอง
- Steam wisps removed (food-coded); Thai h1 clamp reduced (เรทราคา is longer)
- Gotcha: amber word color must sit on .menu-word (the WORD), not .ch — split chars
  don't exist in static/reduced-motion mode, so char-level color rules silently drop
- 3-agent clarity workflow findings applied: ส่งตรงถึง (not กับ) for audience reach,
  "all prices in USD" (Thai leak removed from EN span), Spark Ads clarifier on
  Gen Code, long-term hyphen, แบรนด์ดังการันตี dedupe

## /temp Rate Card v2 (2026-08-12, same day as v1)
- Rework on William's ask: crazier animation, cuter, Thai toggle, mobile conversion
- Added: EN/ไทย toggle (localStorage jz-lang, html.th class flips [data-lang] spans;
  Chonburi for Thai display headings, Noto Sans Thai body, all Thai spans lang-tagged),
  odometer price digits, tuk-tuk drive-by (x in vw), MOST BOOKED/ยอดฮิต stamp,
  steam wisps, confetti burst on CTA, magnetic CTA (own transform, reveal on wrapper),
  swinging neon sign, bulb + food doodles, double counter-scrolling tickers,
  sticky mobile book bar, partner logo row, prefilled mailto + IG DM fallback
- Ran a 14-agent review workflow (5 reviewers -> adversarial verify). 4 confirmed fixes:
  sticky bar observed #cta with rootMargin -150px (not #book at 15%), ?static now adds
  html.static + animation:none CSS (was GSAP-only), --dim raised .42 -> .56 for WCAG AA,
  inset cream focus ring on lang toggle (outline was clipped by overflow:hidden)
- Refuted by verification (do NOT "fix" these): viewport-fit=cover (would break header
  under notch), &nbsp; between flex items (spec discards whitespace; gap handles it),
  Thai ZWSP insertion (runs measured, fit fine; spaces mid-verb-phrase read wrong)
- Thai copy: แม่ค้าเจส / สำรับใหญ่ / จานเด็ด / แขกที่เคยมาทาน; fixed หิวโหยกว่า+ redundancy,
  เที่ยวโรงแรม -> รีวิวโรงแรม
- Gotcha: h1 .word overflow:hidden clips Thai descenders (สระ อู) — padded mask +
  negative margin on the Thai word
- Images: temp/img/*-480.jpg copies (sips -Z 480), main images/ untouched

## Experimental /temp Rate Card v1 (2026-08-12)
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

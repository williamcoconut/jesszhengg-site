# Notes

## Hosting Migration (2026-02-16)
- Moved from Netlify to GitHub Pages
- Reason: Netlify free tier hit 326/300 credits — site paused
  - 120 credits from 8 deploys (15 credits each)
  - 191.6 credits from AI inference
- GitHub Pages: free, unlimited deploys, no credit system
- Domain: jesszheng.co (registered on Porkbun)
- DNS: 4x A records + 4x AAAA records + www CNAME → GitHub Pages
- Old Netlify nameservers (nsone.net) still cached globally — need to wait for propagation
- Check with: `dig jesszheng.co +short` — should show 185.199.x.x when ready
- Temp URL while waiting: https://williamcoconut.github.io/jesszhengg-site/

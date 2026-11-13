#!/usr/bin/env python3
"""Rebuild the two hidden tier pages from index.html.

index.html is the public (mid) rate card. The tier pages are identical except
for the prices, the bundle saving, and a noindex tag. Run after ANY change to
index.html:   python3 build_tiers.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent

# Prices in page order: IG Reel, TikTok, Facebook, YouTube, Bundle,
# then add-ons: IG Stories, UGC/Whitelisting, TikTok Gen Code.
TIERS = {
    "enrkpf7.html": {"prices": ["$550", "$550", "$250", "$650", "$1,000", "$120", "$350", "$150"], "save": "$350"},      # low
    "ojk8uet.html": {"prices": ["$1,500", "$1,500", "$700", "$1,800", "$2,600", "$350", "$900", "$450"], "save": "$1,100"},  # high
}
PUBLIC_SAVE = "$700"  # bundle saving shown on index.html

src = (ROOT / "index.html").read_text(encoding="utf-8")
price_re = re.compile(r'(class="price">)[^<]*(<)')
assert len(price_re.findall(src)) == 8, "index.html should have exactly 8 prices"
assert src.count(PUBLIC_SAVE) == 2, "expected the saving once in English and once in Thai"

for name, tier in TIERS.items():
    prices = iter(tier["prices"])
    # Swap the saving FIRST, while $700 can only mean the saving. Doing it after
    # the price swap would also hit a tier whose Facebook price is $700.
    html = src.replace(PUBLIC_SAVE, tier["save"])
    # then swap each price in the order it appears on the page
    html = price_re.sub(lambda m: m.group(1) + next(prices) + m.group(2), html)
    # tier pages must never be indexed
    html = html.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n<meta name="robots" content="noindex, nofollow">', 1)
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name)

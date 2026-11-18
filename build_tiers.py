#!/usr/bin/env python3
"""Rebuild the hidden rate pages from index.html.

index.html is the PUBLIC page and shows no prices ("On request"), so Google
never sees her rates. The hidden pages are copies of it with the prices, the
bundle saving and the USD line filled in, plus a noindex tag. Send brands the
link to the tier you want them to see. Run after ANY change to index.html:
    python3 build_tiers.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent

# Prices in page order: IG Reel, TikTok, Facebook, YouTube, Bundle,
# then add-ons: IG Stories, UGC/Whitelisting, TikTok Gen Code.
TIERS = {
    "enrkpf7.html": {"prices": ["$550", "$550", "$250", "$650", "$1,000", "$120", "$350", "$150"], "save": "$350"},      # low
    "fkxm0t6.html": {"prices": ["$900", "$900", "$400", "$1,000", "$1,500", "$200", "$550", "$250"], "save": "$700"},    # mid (was the public rates until 2026-11-18)
    "ojk8uet.html": {"prices": ["$1,500", "$1,500", "$700", "$1,800", "$2,600", "$350", "$900", "$450"], "save": "$1,100"},  # high
}

# The rate card subtitle on the hidden pages (index.html says "Rates on request")
SUB = ('<span data-lang="en">All rates in USD. Custom packages available.</span>\n'
       '      <span data-lang="th">ราคาทั้งหมดเป็นดอลลาร์สหรัฐ มีแพ็คเกจพิเศษตามความต้องการ</span>')

src = (ROOT / "index.html").read_text(encoding="utf-8")
price_re = re.compile(r'(class="price">)[^<]*(<)')
sub_re = re.compile(r'<!--rates-sub-->.*?<!--/rates-sub-->', re.S)
assert len(price_re.findall(src)) == 8, "index.html should have exactly 8 prices"
assert re.search(r'\$\d', src) is None, "index.html must not contain any $ price"
assert src.count("{SAVE}") == 2 and '<div class="save" hidden>' in src
assert len(sub_re.findall(src)) == 1

for name, tier in TIERS.items():
    prices = iter(tier["prices"])
    html = price_re.sub(lambda m: m.group(1) + next(prices) + m.group(2), src)  # fill prices in page order
    html = html.replace("{SAVE}", tier["save"]).replace('<div class="save" hidden>', '<div class="save">')
    html = sub_re.sub(lambda m: SUB, html)
    # hidden pages must never be indexed
    html = html.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n<meta name="robots" content="noindex, nofollow">', 1)
    assert "noindex" in html
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name)

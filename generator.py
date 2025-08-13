# -*- coding: utf-8 -*-

CONSTANT = "github.com#?#div.Box-sc-g0xbh4-0.{}:-abp-has(a:-abp-contains({}))"
KEYWORDS = [
    "flszRz",
    "bmcJak",
]

shit_path = "crap"

BANLIST = []
with open(shit_path, "r") as f:
    BANLIST.extend(f.read().splitlines())
for keyword in KEYWORDS:
    [print(CONSTANT.format(keyword, x)) for x in BANLIST]

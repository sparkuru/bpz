# -*- coding: utf-8 -*-

CONSTANT = 'github.com#?#div.Box-sc-g0xbh4-0.{}:-abp-has(a:-abp-contains({}))'
KEYWORD = 'flszRz'
ruozhi_file_path = 'ruozhi'

BANLIST = []
with open(ruozhi_file_path, 'r') as f:
    BANLIST.extend(f.read().splitlines())
[ print(CONSTANT.format(KEYWORD, x)) for x in BANLIST ]

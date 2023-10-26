# -*- coding: utf-8 -*-

CONSTANT = 'github.com#?#div.Box-sc-g0xbh4-0.{}:-abp-has(a:-abp-contains({}))'
KEYWORD = 'hKtuLA'
BANLIST = [
    'cheezcharmer',
    'Dimples1337',
    'zaohmeing',
    'zhaohmng-outlook-com',
    'codin-stuffs',
    'zpc1314521',
    'b0LBwZ7r5HOeh6CBMuQIhVu3-s-random-fork',
    'pxvr-official',
    'cirosantilli'
]

[ print(CONSTANT.format(KEYWORD, x)) for x in BANLIST ]

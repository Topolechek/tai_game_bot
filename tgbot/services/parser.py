import requests
from bs4 import BeautifulSoup as BS

from tgbot.services.price_rub import get_currency_price

val = get_currency_price()
print(val)
def all_games_reg(reg):
    alls = []
    q = []
    id_of_game = ''
    discount = 0
    price = 0
    name = ''
    imag = ''
    r = requests.get(reg)
    html = BS(r.content, 'html.parser')
    for el in html.select('.grid > .component--game-card'):
        title = el.attrs['data-props']
        dictionary = title.split(",")
        for i in dictionary:
            if '"name"' in i:
                name = i.split('"')[3]
            if 'float_price' in i:
                price = i.split(':')[1]
            if '"id"' == i.split(':')[0] and "null" not in i.split(':')[1]:
                id_of_game = i.split(':')[1]
            if 'discount_percent' in i.split(':')[0] and i.split(':')[1].isnumeric():
                discount = i.split(':')[1]
            if len(dictionary[14]) < 58:
                imag = dictionary[14][9:] + ',' + dictionary[15] + ',' + dictionary[16] + ',' + dictionary[17] + ',' + \
                       dictionary[18] + ',' + dictionary[19] + ',' + dictionary[20][:-1]
            else:
                imag = dictionary[14][9:-1]
        open_shop = 'https://psprices.com/game/buy/' + id_of_game
        q.append(name)
        q.append(discount)
        q.append(price)
        q.append(imag)
        q.append(open_shop)
        alls.append(q)
        q = []
    return alls

def game_search(text_search):
    price = 0
    discount = 0
    name = ''
    region = ['us', 'pl', 'gb']
    cash = {'us': '🇺🇸', 'pl': '🇵🇱', 'gb':'🇬🇧'}
    alls = []
    list_us = []
    list_pl = []
    list_uk = []
    prom = []
    for rgn in region:
        name_of_game_full = f'https://psprices.com/region-{rgn}/search/?q={text_search}&content_type=&platform=Switch'
        r = requests.get(name_of_game_full)
        html = BS(r.content, 'html.parser')
        for el in html.select('.grid > .component--game-card '):
            title = el.attrs['data-props']
            dictionary = title.split(",")
            print(dictionary)
            for i in dictionary:
                if '"name"' in i:
                    name = i.split('"')[3] + f' {cash[rgn]}'
                if 'float_price' in i:
                    price = i.split(':')[1]
                if 'discount_percent' in i.split(':')[0] and i.split(':')[1].isnumeric():
                    discount = i.split(':')[1]
                if 'top_category' in i:
                    top_category = i.split(':')[1]

            if price == 'null' or top_category != '"game"':
                continue

            if rgn == region[0] and float(price) > 0:
                list_us.append(name)
                list_us.append(price)
                list_us.append(discount)
                rub = round(float(price) * float(val['usd']))
                list_us.append(rub)
                prom.append(list_us)
                list_us = []



            if rgn == region[1] and float(price) > 0:
                list_pl.append(name)
                list_pl.append(price)
                list_pl.append(discount)
                rub = round(float(price) * float(val['zl']))
                print(float(val['zl']))
                print(rub)
                list_pl.append(rub)
                prom.append(list_pl)
                list_pl = []

            if rgn == region[2] and float(price) > 0:
                list_uk.append(name)
                list_uk.append(price)
                list_uk.append(discount)
                rub = round(float(price) * float(val['ft']))
                list_uk.append(rub)
                prom.append(list_uk)
                list_uk = []

        prom = sorted(prom)
        alls.append(prom)
        prom = []

    print(alls)
    if len(alls[0]) != 0 or len(alls[1]) != 0 or len(alls[2]) != 0:
        return alls
    else:
        return 'err0r'










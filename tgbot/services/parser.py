import requests
from bs4 import BeautifulSoup as BS


def all_games_reg(reg):
    alls = []
    q = []
    r = requests.get(reg)
    html = BS(r.content, 'html.parser')
    for el in html.select('.grid > .component--game-card'):
        title = el.attrs['data-props']
        dictionary = title.split(",")
        if dictionary[0].split(':')[1][-1] == '"':
            name = dictionary[0].split(':')[1][1:-1]
        else:
            name = dictionary[0].split(':')[1][1:]
        price = dictionary[10].split(':')[1]
        id_game = dictionary[12].split(':')[1]
        if reg == 'https://psprices.com/region-us/collection/most-wanted-deals?platform=Switch' or reg == 'https://psprices.com/region-us/collection/lowest-prices-ever?platform=Switch':
            imag = dictionary[14][9:] + ',' + dictionary[15] + ',' + dictionary[16] + ',' + dictionary[17] + ',' + \
                   dictionary[18] + ',' + dictionary[19] + ',' + dictionary[20][:-1]
            discount = dictionary[23].split(':')[1]
        else:
            imag = dictionary[14][9:-1]
            discount = dictionary[17].split(':')[1]
        open_shop = 'https://psprices.com/game/buy/' + id_game
        q.append(name)
        q.append(discount)
        q.append(price)
        q.append(imag)
        q.append(open_shop)
        alls.append(q)
        q = []
    return alls


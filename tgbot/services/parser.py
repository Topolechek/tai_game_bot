import requests
from bs4 import BeautifulSoup as BS


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
        print(dictionary)
        for i in dictionary:
            if '"name"' in i:
                name = i.split('"')[3]
                print(name)
            if 'float_price' in i:
                price = i.split(':')[1]
                print(price)
            if '"id"' == i.split(':')[0] and "null" not in i.split(':')[1]:
                id_of_game = i.split(':')[1]
                print(id_of_game)
            if 'discount_percent' in i.split(':')[0] and i.split(':')[1].isnumeric():
                discount = i.split(':')[1]
                print(discount)
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
        print(alls)
    return alls




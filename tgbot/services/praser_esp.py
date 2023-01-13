import requests
from bs4 import BeautifulSoup as BS

country = {'jp': ['🇯🇵', 'Япония'], 'ar': ['🇦🇷', 'Аргентина'], 'co': ['🇨🇴', 'Колумбия'], 'br': ['🇧🇷','Бразилия'], 'mx': ['🇲🇽', 'Мексика'], 'za': ['🇿🇦', 'Южная Африка'], 'us': ['🇺🇸', 'США'], 'kr': ['🇰🇷', 'Южная Корея'], 'se': ['🇸🇪', 'Швеция']}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}


mpg = 'https://eshop-prices.com/games/popular?currency=RUB'

def all_games_esp():
    alls = []
    q = []
    price = 'Неизвестно'
    name = ''
    imag = ''
    r = requests.get(mpg, headers=headers)
    html = BS(r.content, 'html.parser')
    for el in html.select('.games-list-item'):
        name = str(el.select('.games-list-item-title > h5'))[5:-6]
        price_source = str(el.select('.games-list-item-meta > .price > .price-tag')).split(' ')
        if len(price_source) == 4:
            price = str(el.select('.games-list-item-meta > .price > .price-tag')).split('\n')[2]
        elif len(price_source) == 3:
            price = str(el.select('.games-list-item-meta > .price > .price-tag')).split('\n')[1]
        region_source = str(el.select('.games-list-item-meta > .price > .emoji use'))[-11:-9]
        if region_source in country:
            region = country[region_source]
        else:
            region = str(el.select('.games-list-item-meta > .price > .emoji use'))[-11:-9]

        if name in str(el) and len(name) > 2:
            imag = str(el.select('.games-list-item-image > picture')).split(' ')[-3]
        else:
            imag = 'Картинка отсутствует'
        if len(name) > 2:
            q.append(name)
            q.append(price)
            q.append(imag)
            q.append((region))
            alls.append(q)
            q = []
        else:
            continue
    print(alls)
    return alls


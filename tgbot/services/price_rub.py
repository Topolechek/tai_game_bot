import requests
from bs4 import BeautifulSoup


cash = {
    'DOLLAR_RUB': 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
    ,
    'ZLOTY_RUB': 'https://www.google.com/search?q=злоты+к+рублю&sxsrf=AJOqlzWptFDXmt1elgtSuxA2EylFFJYulA%3A1673337094666&ei=Bhm9Y7KcKJqK9u8PiIiOqA4&ved=0ahUKEwiyt_e4wrz8AhUahf0HHQiEA-UQ4dUDCA4&uact=5&oq=pkjnsк+рублю&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR0oECEEYAEoECEYYAFAAWABgtQVoAHACeACAAQCIAQCSAQCYAQDIAQjAAQE&sclient=gws-wiz-serp'
    ,
    'FUNT_RUB': 'https://www.google.com/search?q=фунты+к+рублю&sxsrf=AJOqlzW8RMnslP-e9vuzJvmIZVEs-a_B7w%3A1673337133616&ei=LRm9Y_qaJYrrsAfTt5Eo&ved=0ahUKEwi65cDLwrz8AhWKNewKHdNbBAUQ4dUDCA4&uact=5&oq=aeyns+к+рублю&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR0oECEEYAEoECEYYAFAAWABg2wZoAHACeACAAQCIAQCSAQCYAQDIAQjAAQE&sclient=gws-wiz-serp'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}


def get_currency_price():
    val = {'usd': '', 'zl': '', 'ft': ''}

    for value in cash:
        full_page = requests.get(cash[value], headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        if value == 'DOLLAR_RUB':
            val['usd'] = convert[0].text.replace(',', '.')
        if value == 'ZLOTY_RUB':
            val['zl'] = convert[0].text.replace(',', '.')
        if value == 'FUNT_RUB':
            val['ft'] = convert[0].text.replace(',', '.')
    return val





print(get_currency_price())

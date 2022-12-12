import requests
from bs4 import BeautifulSoup


def scrapper(page):
    s = 0
    page_site = page  # глубина сканирования страниц на сайте
    for page in range(1, page_site):

        url = 'https://www.32top.ru/stomatologii/page-' + str(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find_all('div', class_='list-item')

        for n, i in enumerate(items, start=1):
            itemName = i.find('a', class_='bold-text list-item__name').text.strip()  # Название клиники
            itemMetro = i.find('div', class_='clinic-metro-item__column').span.text.strip()  # Метро
            itemMetroDistance = i.find('span', class_='list-item__metro__text').text.strip()  # Расстояние до метро
            itemAddress = i.find('a', class_='list-item__address').span.text.strip()  # Адрес клиники
            # itemPhone = i.find('meta', itemprop_='telephone')  # Телефон клиники
            itemService = i.find('div', class_='services-slider__name').text.strip()  # услуга стоматологии
            itemPrice = i.find('div', class_='services-slider__price').text.strip()  # стоимость
            s += 1
            print(f"{s}. {itemName} | {itemMetro} | {itemMetroDistance} | {itemAddress} | {itemService} | {itemPrice}")


if __name__ == "__main__":
    scrapper(3)

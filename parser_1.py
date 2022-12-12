import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL_TEMPLATE = "https://www.32top.ru"
r = requests.get(URL_TEMPLATE)
# # print(r.status_code)  # Статус 200 состояния HTTP — означает, что мы получили положительный ответ от сервера
# # print(r.text)  # получим код странички
#
soup = bs(r.text, "html.parser")
clinic = soup.find_all('a', class_='bold-text list-item__name')
for name in clinic:
    print(name)

# URL_TEMPLATE = "https://www.work.ua/ru/jobs-odesa/?page=2"
# r = requests.get(URL_TEMPLATE)
# # print(r.status_code)
# # print(r.text)
#
# soup = bs(r.text, "html.parser")
# vacancies_names = soup.find_all('div', class_='card card-hover card-visited wordwrap job-link js-hot-block')
# for name in vacancies_names:
#     print(name.a)
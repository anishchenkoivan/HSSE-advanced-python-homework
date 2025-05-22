import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ru/pogoda/ru/moscow'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')

spans = soup.find_all(class_='AppShortForecastDay_temperature__DV3oM')

print('Прогноз погоды на 10 дней')
for i in range(0, len(spans), 2):
    print(f'{i // 2}: {spans[i + 1].text} - {spans[i].text}')

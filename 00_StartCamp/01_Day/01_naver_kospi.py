import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))
kospi = soup.select_one('#KOSPI_now').text
print(f'오늘의 코스피 지수는 {kospi}입니다.')

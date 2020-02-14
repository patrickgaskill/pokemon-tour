import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://en.wikipedia.org/wiki/List_of_international_airports_by_country'

html = requests.get(URL).text
soup = BeautifulSoup(html, 'html.parser')

airports = []
tables = soup.find_all('table', {'class': 'wikitable'})

for table in tables:
    rows = table.find_all('tr')
    for row in rows[1:]:
        cells = [td.text.strip() for td in row.find_all('td')[0:3]]
        airports.append(cells)


with open('intl_airports.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(airports)

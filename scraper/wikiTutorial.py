import urllib.request

url = "https://en.wikipedia.org/wiki/1999%E2%80%932000_FA_Premier_League"

page = urllib.request.urlopen(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page, "lxml")

all_tables = soup.find_all("table")
# print(all_tables)

right_table=soup.find('table', class_='wikitable sortable')
print(right_table)

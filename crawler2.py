import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://seattle.craigslist.org/search/cta' +str(page)
        source_code = requests.get(url)
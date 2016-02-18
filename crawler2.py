import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 0
    while page < max_pages:
        url = 'http://seattle.craigslist.org/search/cta' +str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        #plain text is source code from web space
        soup = BeautifulSoup(plain_text)
        #attribute looking for = 2nd arg
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = link.get('href')
        page += 1
        
trade_spider(1)
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    

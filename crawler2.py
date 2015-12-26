import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://seattle.craigslist.org/search/cta' +str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        #plain text is source code from web space
        soup = BeautifulSoup(plain_text)
        
        for link in soup.findAll('a', ):
            

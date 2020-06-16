
import requests
import lxml
from bs4 import BeautifulSoup

def rss_medium():
    url = 'https://levelup.gitconnected.com/feed'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.content, features='xml')
    return {
        'items': soup.findAll('item')[:5]
    }


items = rss_medium()

for item in items['items']:
    print("Title: ", item.title.text)
    print(" Link: ", item.link.text)

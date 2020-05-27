#!/usr/bin/python3

# Ramkrushna Bolewar
# This scripts scrapps data from BMS website

from bs4 import BeautifulSoup
import re
import requests

# URL deconstruct
# base url : https://in.bookmyshow.com
# content url : /location/content type/content
# ex : /hyderbad/movies/avengers

URL = "https://in.bookmyshow.com/hyderabad/movies/blackwidow"
res = requests.get(URL)
print("status code: ", res.status_code)

soup = BeautifulSoup(res.content, 'html')
print(soup.prettify())

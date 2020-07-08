
import requests, os
import html5lib
from bs4 import BeautifulSoup
import csv
'''
print("\n==== Requests module ====\n")

res = requests.get('https://raw.githubusercontent.com/ramkrushna26/Bash/master/README')
print("status coe : " + str(res.status_code))
print("lenght of downloaded : " + str(len(res.text)))
print("content: \n" + res.text)

#to check whether requests got anyh error while downloading
print("error status : " + str(res.raise_for_status()))

outFile = open('../Test/readme', 'wb')
for buf in res.iter_content(1000):
    outFile.write(buf)

os.unlink('../Test/readme')
outFile.close()
'''
print("\n==== bs4 module ====\n")

URL = "http://www.values.com/inspirational-quotes"
res = requests.get(URL)
print("status code : ", res.status_code)

soup = BeautifulSoup(res.text, 'html5lib')
table = soup.findAll('div', attrs = {'class' : 'container'})
quotes = []

for record in table:
    for row in record.findAll('div', attrs = {'class' : 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
        quote = {}
        quote['theme'] = row.h5.text
        quote['url'] = row.a['href']
        quote['img'] = row.img['src']
        quote['lines'] = row.img['alt'].split(" #")[0]
        quote['author'] = row.img['alt'].split(" #")[1]
        quotes.append(quote)

filename = os.environ.get("HOME") + "/Test/inspirationalQuotes.csv"
with open(filename, 'w') as f:
    w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)

print("Script completed!")

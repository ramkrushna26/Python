
import requests, os, bs4

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

print("\n==== bs4 module ====\n")
price = 0
def getAmzPrice(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup('html', res.text, 'html.parser')
    elements = soup.select('html.fonts-loaded body div#container div div.t-0M7P._3GgMx1._2doH3V div._3e7xtJ div._1HmYoV.hCUpcT div._1HmYoV._35HD7C.col-8-12 div.bhgxx2.col-12-12 div._29OxBi div._3iZgFn div._2i1QSc div._1vC4OE._3qQ9m1')
    return elements[0].text.strip()

price = getAmzPrice('https://www.flipkart.com/apple-iphone-se-red-64-gb/p/itm6e9443811d36a')
print("Price of product : " + str(price))

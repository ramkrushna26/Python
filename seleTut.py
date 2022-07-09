
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://coreyms.com/')

#clicking on the specific css selector link
elem = browser.find_element_by_css_selector('.post-1661 > header:nth-child(1) > h2:nth-child(1) > a:nth-child(1)')
elem.click()

#type into webpage
searchElem = browser.find_element_by_css_selector('>search field<')
searchElem.send_keys("text to search")
saerchElem.submit()

#to go back and forth, refresh and quit on browser
browser.back()
browser.forward()
browser.refresh()
browser.quit()

#reas content of web pages with selenium

browser = webdriver.Firefox()
browser.get('https://coreyms.com/')
elem = browser.find_element_by_css_selector('.post-1661 > header:nth-child(1) > h2:nth-child(1) > a:nth-child(1)')
print(elem.text)

# to get entire content
elem = browser.find_element_by_css_selector('html')
print(elem.text)


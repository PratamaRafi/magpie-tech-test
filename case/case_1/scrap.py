import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# scraping rockbross
url = "https://www.tokopedia.com/rockbros/product"
driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup)

data = []
# post-processing data
for item in soup.findAll('div', class_ = 'css-1asz3by'):
    produk = item.find('div', class_ = 'css-3um8ox').text
    jml = item.find('div', class_ = 'css-1sgek4h').int
    harga = item.find('div', class_ = 'css-h66vau').int
    temp = {'nama':produk,'jumlah':jml, 'harga': (harga*jml)}
    data.append(temp)

print(data)

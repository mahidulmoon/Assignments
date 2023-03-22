import requests
import lxml
from bs4 import BeautifulSoup


url = "https://shop.adidas.jp/products/HB9386/"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
f = requests.get(url, headers = headers)

soup = BeautifulSoup(f.content,'lxml')

breadcrumb_div = soup.find('div', {
  'class': 'breadcrumb_wrap'
})

# breadcrumbs = breadcrumb_div.find_all('a')
breadcrumbs = breadcrumb_div.find('li', {
  'class': 'breadcrumbListItem breadcrumbLink test-breadcrumbLink'
})


print(breadcrumbs)
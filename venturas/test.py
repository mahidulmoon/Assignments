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


# print(breadcrumbs)

product_info_details_div = soup.find('div', {
  'class': 'articlePurchaseBox css-gxzada'
})
product_info_div = product_info_details_div.find('div', {
  'class': 'articleNameHeader css-t1z1wj'
})

product_info_div_links = product_info_div.find_all('a')

print(product_info_div_links)
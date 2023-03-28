import requests
import lxml
from bs4 import BeautifulSoup


url = "https://shop.adidas.jp/products/HB9386/"
media_root_url = "https://shop.adidas.jp"

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
f = requests.get(url, headers = headers)

soup = BeautifulSoup(f.content,'lxml')

breadcrumb_div = soup.find('div', {
  'class': 'breadcrumb_wrap'
})

breadcrumbs = breadcrumb_div.find('li', {
  'class': 'breadcrumbListItem breadcrumbLink test-breadcrumbLink'
})



main_content_div = soup.find('div', {
  'class': 'contentsWrapper'
})

product_info_details_div = soup.find('div', {
  'class': 'articlePurchaseBox css-gxzada'
})
product_info_div = product_info_details_div.find_all('div', {
  'class': 'articleNameHeader css-t1z1wj'
})


category_name = ''
item_title = ''
price = ''
size = ''
slider_img_url = []
title_of_description = ''
title_of_general_description = ''
title_of_description_itemization = ''

for item in product_info_div:
    x = item.find('span')
    if x:
        category_name = x.text.strip()
    y = item.find('h1')
    if y:
        item_title = y.text.strip()

product_price_div = product_info_details_div.find_all('div', {
  'class': 'articlePrice test-articlePrice css-1apqb46'
})

for item in product_price_div:
    z = item.find('span')
    if x:
        price = z.text.strip()

product_size_div = product_info_details_div.find_all('div', {
  'class': 'test-sizeSelector css-539bvd'
})

for item in product_size_div:
    sample_size_list = []
    s = item.find_all('li')
    for single in s:
        sample_size_list.append(single.text.strip())
    size = ','.join(sample_size_list)

product_slider_image_div = main_content_div.find_all('div', {
  'class': 'slider-frame'
})

for image in product_slider_image_div:
    i = image.find_all('img')
    for single_img in i:
        slider_img_url.append(media_root_url+single_img['src'])

product_title_description_div = main_content_div.find_all('div', {
  'class': 'inner'
})

for row in product_title_description_div:
    t = row.find_all('h4')
    for value in t:
        title_of_description = value.text.strip()

title_description_div = main_content_div.find_all('div', {
  'class': 'description clearfix test-descriptionBlock'
})

for row in title_description_div:
    title_description_div = row.find_all('div', {
        'class': 'commentItem-mainText test-commentItem-mainText'
    })
    for x in title_description_div:
        title_of_general_description = x.text.strip()
    another_des = row.find_all('li')
    queue = []
    for value in another_des:
        queue.append(value.text.strip()+'\n')
    title_of_description_itemization = ''.join(queue)



# print(title_of_description_itemization)


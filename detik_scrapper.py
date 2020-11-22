import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})
print(html_doc.text)

soup = BeautifulSoup(html_doc.text, 'html.parser')
populer_area = soup.find(attrs={'class':'list-content'})
titles = populer_area.find_all(attrs={'class':'media_title'})
images = populer_area.find_all(attrs={'class':'media_image'})

for image in images:
     print(images.find('a').find('img')['title'])
 # print(titles)

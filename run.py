import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('\detik-populer')
def detik_populer():
    html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})
    print(html_doc.text)

    soup = BeautifulSoup(html_doc.text, 'html.parser')
    populer_area = soup.find(attrs={'class': 'list-content'})
    titles = populer_area.find_all(attrs={'class': 'media_title'})
    images = populer_area.find_all(attrs={'class': 'media_image'})

    return render_template('index.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)

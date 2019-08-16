from bs4 import BeautifulSoup
import random
import re
import requests
from flask import Flask, render_template
app = Flask(__name__)

PH = 'https://www.pornhub.com'


@app.route('/')
def hello():
    r = requests.get(PH)
    links = [l for l in r.text.split('\n') if 'view_video.php' in l]
    matches = [re.search('a href="(.*)" title="', l) for l in links]
    titles = [m.group(1) for m in matches if m]

    # Find pornhub video with comments
    while True:
        pick = random.choice(titles)
        url = PH + pick
        video = requests.get(url)
        html = BeautifulSoup(video.text, "html.parser")
        title = html.title.text.split('-')[0].strip()
        comments = html.findAll('div', attrs={'class': 'commentMessage'})
        if comments:
            comment = random.choice(comments).span.text
            break

    return render_template('home.html', url=url, title=title, comment=comment)


if __name__ == '__main__':
    app.run(host="127.0.0.1")

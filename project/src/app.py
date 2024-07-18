import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor
from MemeEngine import Meme
from itertools import chain
from time import sleep

app = Flask(__name__,  static_folder='./static')


def download_file(url):
    local_filename = "./tmp/" + url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = list(chain(*[Ingestor.parse(f) for f in quote_files]))
    images_path = "./_data/photos/dog/"
    imgs = [f"{images_path}{f}" for f in os.listdir(images_path) if f.endswith(".jpg")]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    print(quote)
    path = Meme.make_meme(img, quote.body, quote.author)
    print(path)
    print(os.listdir('./static'))
    while path not in os.listdir('./static'):
        sleep(1)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    user_img = download_file(request.form.get('image_url'))
    path = Meme.make_meme(user_img, request.form.get('body'), request.form.get('author'))
    os.remove(user_img)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug=True)

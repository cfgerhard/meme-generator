"""The file, that starts the app."""
import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor
from MemeEngine import Meme
from itertools import chain
import ExceptionClasses

app = Flask(__name__,  static_folder='./static')


def download_file(url):
    """Download custom file."""
    local_filename = "./tmp/" + url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = list(chain(*[Ingestor.parse(f) for f in quote_files]))
    images_path = "./_data/photos/dog/"
    imgs = [f"{images_path}{f}" for f in os.listdir(images_path)
            if f.endswith(".jpg")]
    return quotes, imgs


quotes, imgs= setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    app_meme = Meme(output_dir='./static', img=img, quote=quote)
    path = Meme.make_meme(self=app_meme, img_path=img, text=quote.body, author=quote.author)
    return render_template('meme.html', path=str(path).split('/')[-1])


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    try:
        user_img = download_file(request.form.get('image_url'))
    except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError):
        return render_template('meme_error.html', message="This seems to be an invalid URL, please check and try again")
    try:
        is_good_ext = str(user_img).split('.')[-1] in ['jpg', 'png', 'jpeg']
        if not is_good_ext: raise ExceptionClasses.WrongExtensionError("This file type is not supported, please find"
                                                                       " another file to upload")
    except ExceptionClasses.WrongExtensionError:
        os.remove(user_img)
        return render_template('meme_error.html', message="This file type is not supported, please find another "
                                                          "file to upload")

    app_meme = Meme(output_dir='./static', img=user_img, quote=None)
    path = Meme.make_meme(self=app_meme, img_path=user_img, text=request.form.get('body'),
                          author=request.form.get('author'))
    print(path)
    os.remove(user_img)
    return render_template('meme.html', path=str(path).split('/')[-1])


if __name__ == "__main__":
    app.run(debug=True)

"""Model for Memes."""
from PIL import Image, ImageDraw, ImageFont  # Pillow is being imported like this
# (see https://pillow.readthedocs.io/en/stable/reference/ImageFont.html)
import tempfile
from random import randint
import textwrap


wrap = textwrap.TextWrapper(width=40)


class Meme:
    """Class for memes."""

    def __init__(self, output_dir, img, quote):
        """Construct Memes."""
        self.quote = quote
        self.img = img
        self.output_dir = output_dir

    @staticmethod
    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make meme."""
        tempfile.tempdir = self.output_dir
        outpath = tempfile.NamedTemporaryFile(mode='w+b',
                                              delete=False, suffix='.jpg')
        img = Image.open(img_path)
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        message = wrap.fill(text=f"{text} - {author}")
        draw.text((randint(2,49), randint(2,49)), message, font=font, fill='red')
        img.save(outpath)
        return str(outpath.name)

    def __repr__(self):
        """Represent Meme."""
        return f"Meme with quote={self.quote} and img={self.img}"

    def __str__(self):
        """Represent String of Meme."""
        return f"Meme with quote={self.quote} and img={self.img}"

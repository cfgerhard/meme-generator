"""Model for Memes."""
from abc import ABC, abstractmethod
from PIL import Image, ImageDraw, ImageFont


class Meme(ABC):
    """Class for memes."""

    def __init__(self, img, quote):
        """Construct Memes."""
        self.quote = quote
        self.img = img

    @abstractmethod
    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make meme."""
        outpath = './out/' + img_path.split('/')[-1]
        img = Image.open(img_path)
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        message = f"{text} - {author}"
        draw.text((10, 30), message, font=font, fill='red')
        img.save(outpath)
        return outpath

    def __repr__(self):
        """Represent Meme."""
        return f"Meme with quote={self.quote} and img={self.img}"

    def __str__(self):
        """Represent String of Meme."""
        return f"Meme with quote={self.quote} and img={self.img}"

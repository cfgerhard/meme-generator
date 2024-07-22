# Meme Generator
This project is built to create a picture, that includes a quote and the according author information.

This can be achieved locally as well as served through a flask app server.

```
.(projectroot)
├── readme.md
├── src
│   ├── MemeEngine
│   │   ├── MemeModel.py
│   │   └── __init__.py
│   ├── QuoteEngine
│   │   ├── CSVIngestor.py
│   │   ├── DocxIngestor.py
│   │   ├── Ingestor.py
│   │   ├── IngestorInterface.py
│   │   ├── PDFIngestor.py
│   │   ├── TXTIngestor.py
│   │   ├── __init__.py
│   │   └── quote.py
│   ├── _data
│   │   ├── DogQuotes
│   │   │   ├── DogQuotesCSV.csv
│   │   │   ├── DogQuotesDOCX.docx
│   │   │   ├── DogQuotesPDF.pdf
│   │   │   └── DogQuotesTXT.txt
│   │   ├── SimpleLines
│   │   │   ├── SimpleLines.csv
│   │   │   ├── SimpleLines.docx
│   │   │   ├── SimpleLines.pdf
│   │   │   └── SimpleLines.txt
│   │   └── photos
│   │       └── dog
│   │           ├── xander_1.jpg
│   │           ├── xander_2.jpg
│   │           ├── xander_3.jpg
│   │           └── xander_4.jpg
│   ├── app.py
│   ├── fonts
│   │   └── LilitaOne-Regular.ttf
│   ├── meme.py
│   ├── requirements.txt
│   ├── static
│   │   ├── tmp2tag2y4i.jpg
│   │   ├── tmp35qml5bu.jpg
│   │   ├── tmp_pbwq0a2.jpg
│   │   ├── tmpavh3vg4k.jpg
│   │   ├── tmpgoexqrtu.jpg
│   │   ├── tmpi0lshvss.jpg
│   │   ├── tmpjfbwwurq.jpg
│   │   ├── tmpn3ok5t9x.jpg
│   │   ├── tmps91z4t0g.jpg
│   │   └── tmpsdr8bumt.jpg
│   ├── templates
│   │   ├── base.html
│   │   ├── meme.html
│   │   └── meme_form.html
│   └── tmp
└── tree.txt

```





## Test Case
Image URL
https://as2.ftcdn.net/v2/jpg/08/32/53/89/1000_F_832538986_Mp9sgjpmk9DLQzJR9SZKI9QinSQmgA6h.jpg

Quote Body
HotDogs are delicious

Quote Author
Christian
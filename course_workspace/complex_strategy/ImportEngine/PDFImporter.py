
from typing import List
import subprocess
import random
import os

from .ImportInterface import ImportInterface
from .Cat import Cat

class PDFImporter(ImportInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        pdf = subprocess.call(['pdftotext',path, tmp])

        file_ref = open(tmp, 'r')
        cats = []
        for line in file_ref.readlines():
            parse = line.split(',')
            print('Value 1', parse[0], 'Value 2', parse[1], 'Value 3', parse[2])
            new_cat = Cat(parse[0], int(parse[1]), bool(parse[2]))
            cats.append(new_cat)
        file_ref.close()
        os.remove(tmp)
        return cats
import json

from datetime import datetime
from operator import itemgetter


def load_jsonfile(filename):
    """Считываем из файла данные и
    переводим на язык python"""
    with open(filename, encoding='utf8') as file:
        return json.loads(file.read())



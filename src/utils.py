import json

from datetime import datetime
from operator import itemgetter


def load_jsonfile(filename):
    """Считываем из файла данные и
    переводим на язык python"""
    with open(filename, encoding='utf8') as file:
        return json.loads(file.read())


def removing_empty(filename):
    """Удаляем пустые словари
    """
    new_list = []
    for item in filename:
        if bool(item) is False:
            continue
        else:
            new_list.append(item)
    return new_list


def type_payment(pay):
    if 'счёт' in pay.upper():
        return f'{pay[:5]}**{pay[-2:]}'
    else:
        payment_type: str = f'{pay.split()[len(pay.split()) - 1]}'
        card_type = f'{pay.replace(f" {payment_type}", "")}'
        payment_type = payment_type[:-10] + '** **** ' + payment_type[12:]
        payment_type = f'{card_type} {payment_type[:4]} {payment_type[4:]}'
        return payment_type



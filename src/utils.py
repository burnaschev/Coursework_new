import json

from datetime import datetime
from operator import itemgetter


def load_jsonfile(filename):
    """Считываем из файла данные и
    переводим на язык python"""
    with open(filename, encoding='utf8') as file:
        return json.loads(file.read())


def removing_empty(filename):
    """Пропускаем пустые словари
    """
    new_list = []
    for item in filename:
        if bool(item) is False:
            continue
        else:
            new_list.append(item)
    return new_list


def type_payment(pay):
    """Вывод счетов и карт в нужном формате
    """
    if 'счёт' in pay.upper():
        return f'{pay[:5]}**{pay[-2:]}'
    else:
        payment_type: str = f'{pay.split()[len(pay.split()) - 1]}'
        card_type = f'{pay.replace(f" {payment_type}", "")}'
        payment_type = payment_type[:-10] + '** **** ' + payment_type[12:]
        payment_type = f'{card_type} {payment_type[:4]} {payment_type[4:]}'
        return payment_type


def sorted_date(file):
    """Сортировка списка по дате
    """
    filename = load_jsonfile(file)
    filename = removing_empty(filename)
    date_ = [date for date in filename if 'date' in date]
    date_.sort(key=itemgetter('date'), reverse=True)
    return date_[0:6]


def get_five_operations(file):
    """Получаем 5 последних
    операций"""
    count = 0
    for i in file:
        if count == 5:
            return
        if len(i) > 0 and i['state'] == 'EXECUTED':
            datetime_str = i['date'].split('T')[0]
            datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d').date().strftime('%d.%m.%Y')
            cost = f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}'
            print(f'{datetime_object} {i["description"]}')
            if 'открытие' in i['description'].lower():
                print(f'{type_payment(i["to"])}')
            else:
                print(f'{type_payment(i["from"])} -> {type_payment(i["to"])}')
            print(cost, '\n')

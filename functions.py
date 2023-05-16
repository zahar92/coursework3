import json
import re
from datetime import datetime


def get_data(file_url):
    """
    Получает json из файла
    :param file_url: путь к файлу
    :return: list
    """
    with open(file_url, "r", encoding="utf-8") as file:
        operations = json.load(file)
        return operations


def date_convert(date_string):
    """
    Конвертирует строку в объект datetime
    :param date_string: дата в строковом формате
    :return: datetime
    """
    if date_string:
        return datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')
    else:
        return datetime.min


def date_format(date_string):
    """
    Форматирует дату по шаблону: 14.10.2018
    :param date_string: Строка в iso-формате
    :return: string
    """
    datetime_odj = datetime.fromisoformat(date_string)
    date_formatted = datetime_odj.strftime('%d.%m.%Y')
    return date_formatted


def sort_data():
    """
    Сортирует список по полю date
    :return: list
    """
    operations = get_data('operations.json')
    sorted_data = sorted(operations, key=lambda x: date_convert(x.get('date', '')), reverse=True)
    return sorted_data


def bank_card_format(bank_card):
    """
    Форматирует карту по шаблону: Visa Platinum 7000 79** **** 6361 ->
    :param bank_card: Название и номер банковской карты
    :return: string
    """
    if bank_card is not None:
        bank_name = re.findall(r'^([\w\W]+?)\s\d', bank_card)[0]
        card_number = re.findall(r'\d+$', bank_card)[0]
        hide_card_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
        card_number_chunked = re.findall(r'[\d\D]{4}', hide_card_number)
        return f'{bank_name} {" ".join(card_number_chunked)} -> '
    return ''


def bank_account_format(account_number):
    """
    Форматирует счет по шаблону: Счет **9638
    :param account_number:
    :return: string
    """
    if account_number is not None:
        account_name = re.findall(r'^([\w\W]+?)\s\d', account_number)[0]
        account_number = re.findall(r'\d+$', account_number)[0]
        hide_card_number = '**' + account_number[-4:]
        return f'{account_name} {hide_card_number}'
    return ''


from pprint import pprint
from functions import sort_data, date_format, bank_card_format, bank_account_format
from venv.bin import pytest


def show_operation():
    """
    Выводит операции по шаблону
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.
    :return: string
    """
    operations = sort_data()
    i = 0
    for operation in operations:
        if operation.get('state') == 'EXECUTED' and i < 5:
            operation_date = date_format(operation.get('date'))
            operation_description = operation.get('description')
            operation_amount = operation.get('operationAmount')
            operation_sum = operation_amount.get('amount')
            operation_currency = operation_amount.get('currency').get('name')
            operation_from = bank_card_format(operation.get('from'))
            operation_to = bank_account_format(operation.get('to'))

            print(f"{operation_date} {operation_description}\n{operation_from}{operation_to}\n{operation_sum} {operation_currency}", end="\n\n")
            i += 1


if __name__ == '__main__':
    # pprint(date_format('2019-08-26T10:50:58.294041'))
    show_operation()

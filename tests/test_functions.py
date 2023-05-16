from functions import get_data, date_convert, date_format, bank_card_format, bank_account_format
import pytest


def test_get_data():
    assert get_data("operations.json")


def test_date_convert_positive():
    assert date_convert('2023-05-16T00:00:00.000')


def test_date_convert_negative():
    with pytest.raises(ValueError):
        date_convert('2023-05-16 00:00:00.000')


def test_date_format():
    assert date_format('2023-05-16T00:00:00.000')


@pytest.mark.parametrize('card, formatted_card', [('Visa Platinum 7000793214566361', 'Visa Platinum 7000 79** **** 6361 -> '),
                                                  ('Счет 42760000111155557777', 'Счет 4276 00** **** **** 7777 -> ')])
def test_bank_card_format(card, formatted_card):
    assert bank_card_format(card) == formatted_card


@pytest.mark.parametrize('card, formatted_card', [('Счет 64686473678894779589', 'Счет **9589'),
                                                  ('Visa Platinum 8990922113665229', 'Visa Platinum **5229')])
def test_bank_account_format(card, formatted_card):
    assert bank_account_format(card) == formatted_card

from tests import pytest
from src.mask import get_mask_card_number
from src.mask import get_mask_account
from src.widget import mask_account_card
from src.widget import date
from src.processing import filter_by_state
from tests.contest import test_mask_number

def test_get_mask_card_number():
    assert get_mask_card_number('88005553535') == test_mask_number()
    assert get_mask_card_number('427981274832738') == '4279 81** **** 2738'
    assert get_mask_card_number('hewhw2u37y32huu829') == 'hewh w2** **** u829'
    assert get_mask_card_number('') == ''


def test_get_mask_account():
    assert get_mask_account('04580923') == '** 0923'
    assert get_mask_account('438328903284083042') == '** 3042'
    assert get_mask_account('qwy43gf78yr4370d08') == '** 0d08'
    assert get_mask_account('') == ''

def test_mask_account_card():
    assert mask_account_card('632968791') == 'Счет **8791'
    assert mask_account_card('Master Card', '1234567891011') == 'Master Card 1234 56** **** 1011'
    assert mask_account_card('te639t38yye03y2') == 'Счет **03y2'

def test_date():
    assert date('2018-07-11T02:26:18.671407') == '11.07.2018'
    assert date('2044-07-22uqdhuiowee') == '22.07.2044'
    assert date('2077-01-31dh36y97y28') == '31.01.2077'

def test_filter_by_state():
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}], 'EXECUTED') == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}], 'CANCELED') == []
    assert filter_by_state([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'CANCELED') == [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]



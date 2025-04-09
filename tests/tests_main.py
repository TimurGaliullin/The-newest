from src.mask import get_mask_card_number
from src.mask import get_mask_account
from src.widget import mask_account_card
from src.widget import date
from src.processing import filter_by_state
from src.processing import sort_by_date

def test_get_mask_card_number():
    assert get_mask_card_number('88005553535') == '8800 55** **** 3535'
    assert get_mask_card_number('427981274832738') == '4279 81** **** 2738'
    assert get_mask_card_number('hewhw2u37y32huu829') == 'hewh w2** **** u829'
    assert get_mask_card_number('') == ''


def test_get_mask_account():
    assert get_mask_account('04580923') == '** 0923'
    assert get_mask_account('438328903284083042') == '** 3042'
    assert get_mask_account('qwy43gf78yr4370d08') == '** 0d08'
    assert get_mask_account('') == ''



from src.mask import get_mask_card_number
from src.mask import get_mask_account
from src.widget import mask_account_card
from src.widget import date

print(get_mask_card_number('hfskhslkj'))
print(get_mask_account('sdfdsfds'))
print(mask_account_card('Master_Card', '012345678910'))
print(date('2018-07-11T02:26:18.671407'))
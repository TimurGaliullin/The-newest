def get_mask_card_number(card_number: str) -> str:
    if card_number == '':
        return ''
    a = card_number[:4]
    b = card_number[4:6]
    c = card_number[-4:]
    '''Функция маскирует номер карты путём сложения частей её номера'''
    full_card_number = a + ' ' + b + '** **** ' + c
    return full_card_number

def get_mask_account(account_number: str) -> str:
    if account_number == '':
        return ''
    piece = account_number[-4:]
    '''Функция возвращает значение при помощи f-строки'''
    return f'** {piece}'




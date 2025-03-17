def mask_account_card(type: str, number: str) -> str:
    if len(number) != 12:
        mask_number = number[-4:]
        return f'Счет **{mask_number}'
    if len(number) == 12:
        '''Функция определяет номер счёта и номер карты'''
        return f'{type} {number[:4]} {number[4:6]}** **** {number[-4:]}'

def date(date: str) -> str:
    day = date[8:10]
    month = date[5:7]
    year = date[0:4]
    '''Функция выстраивает дату путём выделения частей входных данных'''
    return f'{day}.{month}.{year}'
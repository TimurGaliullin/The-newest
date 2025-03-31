def filter_by_state(dictionaries: list) -> list:
    new_list = []
    for i in range(len(dictionaries)):
        if  dictionaries[i]['state'] != 'EXECUTED':
            new_list.append(dictionaries[i])
    return new_list

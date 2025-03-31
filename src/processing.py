def filter_by_state(dictionaries: list, name_state: str) -> list:
    new_list = []
    for i in range(len(dictionaries)):
        if name_state == '' or ' ':
            name_state = 'EXECUTED'
        if  dictionaries[i]['state'] == name_state:
            new_list.append(dictionaries[i])
    return new_list

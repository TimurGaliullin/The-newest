def filter_by_state(dictionaries: list, name_state: str) -> list:
    new_list = []
    for i in range(len(dictionaries)):
        if name_state == '' or ' ':
            name_state = 'EXECUTED'
        if  dictionaries[i]['state'] == name_state:
            new_list.append(dictionaries[i])
    return new_list

def sort_by_date(lists: list) -> list:
    newest_list = []
    for i in range(len(lists)):
        if int(str(lists[i]['date'][:3])) < int(str(lists[i - 1]['date'][:3])):
            newest_list.append(lists[i - 1])
        elif int(str(lists[i]['date'][:3])) == int(str(lists[i - 1]['date'][:3])):
            if int(str(lists[i]['date'][4:6])) < int(str(lists[i - 1]['date'][4:6])):
                newest_list.append(lists[i - 1])
            elif int(str(lists[i]['date'][4:6])) == int(str(lists[i - 1]['date'][4:6])):
                if int(str(lists[i]['date'][7:9])) < int(str(lists[i - 1]['date'][7:9])):
                    newest_list.append(lists[i - 1])
                else:
                    newest_list.append(lists[i])
            else:
                newest_list.append(lists[i - 1])
        else:
            newest_list.append(lists[i])
    return newest_list




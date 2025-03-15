def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    new_list = []
    for i in list_dict:
        if i["state"] == state:
            new_list.append(i)
    return new_list


def sort_by_date(list_dict: list[dict], reverse_sort: bool = True) -> list[dict]:
    return sorted(list_dict, key=lambda date: date.get("date", 0), reverse=reverse_sort)

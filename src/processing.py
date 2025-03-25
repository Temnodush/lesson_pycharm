def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и возвращает новый список со словарями,
    у которых ключ state равен значению `state`.
    """
    new_list = []
    for i in transactions:
        if i["state"] == state:
            new_list.append(i)
    return new_list


def sort_by_date(list_dict: list[dict], reverse_sort: bool = True) -> list[dict]:
    """
    Функция сортирует принимаемый список словарей и возвращает
    отсортированный в порядке убывания.
    """
    return sorted(list_dict, key=lambda date: date.get("date", 0), reverse=reverse_sort)

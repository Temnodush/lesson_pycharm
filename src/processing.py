def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и возвращает новый список со словарями,
    у которых ключ state равен значению `state`.
    """
    new_list = []
    for transaction in transactions:
        if "state" not in transaction:
            raise KeyError(f"Ключ 'state' не найден в транзацкии: {transaction}")
        if transaction["state"] == state:
            new_list.append(transaction)
    return new_list


def sort_by_date(list_dict: list[dict], reverse_sort: bool = True) -> list[dict]:
    """
    Функция сортирует принимаемый список словарей и возвращает
    отсортированный в порядке убывания.
    """
    return sorted(list_dict, key=lambda date: date.get("date", "2024-01-01T00:00:00.000000"), reverse=reverse_sort)

import random


def filter_by_currency(transactions: list[dict], currency_code: str):
    """Фильтрует транзакции по коду валюты (поддерживает разные форматы данных)."""
    for transaction in transactions:
        code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if code == currency_code:
            yield transaction
        elif transaction.get("currency_code") == currency_code:  # Для CSV
            yield transaction


def transaction_descriptions(transactions):
    """Принимает список словарей и проводит итерацию по словарям. Возвращает описание транзакции."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start=1, stop=9999999999999999):
    """Генерирует номер карты в диапазоне и приводит в корректный формат."""
    while True:
        new_number = random.randint(start, stop)
        new_number_str = str(new_number)
        correct_len_number = 16 - len(new_number_str)
        generated_number = "0" * correct_len_number + new_number_str
        yield f"{generated_number[:4]} {generated_number[4:8]} {generated_number[8:12]} {generated_number[12:]}"

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("transactions_currency", ["USD", "RUB"])
def test_filter_by_valid_currency(simple_transactions, transactions_currency) -> None:
    """Проверка поиска допустимых валют в списке"""
    test_transactions = list(filter_by_currency(simple_transactions, transactions_currency))
    for transaction in test_transactions:
        assert transaction["operationAmount"]["currency"]["code"] == transactions_currency


def test_filter_by_currency_invalid_currency(simple_transactions) -> None:
    """Проверка списка с несуществующей валютой"""
    eur_transactions = list(filter_by_currency(simple_transactions, "EUR"))
    assert len(eur_transactions) == 0  # Длина списка с несуществующей валютой.


def test_filter_by_currency_empty_list() -> None:
    """Проверка пустого списка с существующей валютой"""
    empty_transactions = list(filter_by_currency([], "USD"))
    assert len(empty_transactions) == 0


def test_transaction_descriptions_extraction(simple_transactions):
    """Проверка извлечения описаний"""
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
        "Перевод с карты на карту",
    ]
    result = list(transaction_descriptions(simple_transactions))
    assert result == expected


def test_transaction_descriptions_empty_list():
    """Проверка работы с пустым списком"""
    assert list(transaction_descriptions([])) == []


def test_card_number_generator_format_correctness():
    """Проверка формата, длины номера карты"""
    generator = card_number_generator(1, 9999999999999999)
    number = next(generator)
    # Проверка формата XXXX XXXX XXXX XXXX
    assert len(number) == 19
    assert number[4] == " " and number[9] == " " and number[14] == " "


@pytest.mark.parametrize(
    "minimum, maximum, expected",
    [
        (1, 1, "0000 0000 0000 0001"),
        (9999999999999999, 9999999999999999, "9999 9999 9999 9999"),
        (12345, 12345, "0000 0000 0001 2345"),
    ],
)
def test_card_number_generator_simple_check(minimum, maximum, expected):
    """Проверка ожидаемой генерации с использованием параметризации"""
    result = next(card_number_generator(minimum, maximum))
    assert result == expected


def test_card_number_generation_in_range():
    """Проверка корректной генерации чисел в заданном диапазоне"""
    min_val = 1
    max_val = 9999999999999999
    generator = card_number_generator(min_val, max_val)
    for i in range(100):
        number = next(generator)
        assert number[4] == " " and number[9] == " " and number[14] == " "

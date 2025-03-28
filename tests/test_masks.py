import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(masked_card_number: str) -> None:
    """Проверка функциональности card_number"""
    assert get_mask_card_number("1234123412341234") == masked_card_number


@pytest.mark.parametrize(
    "card_number, exception",
    [
        ("123412341234123!", ValueError),  # Ошибка с использованием символов.
        ("11112222333344445555", ValueError),  # Ошибка длины.
        ("abcdefghijklmnop", ValueError),  # Ошибка с использованием букв.
        ("", ValueError),
        (" ", ValueError),
    ],
)
def test_get_mask_card_number_value_error(card_number: str, exception: type[Exception]) -> None:
    """Проверка функции card_number и с ошибками ValueError"""
    with pytest.raises(exception):
        get_mask_card_number(card_number)


def test_get_mask_card_len(simple_card_number: str, correct_len_card_number: int, masked_card_number: str) -> None:
    """Проверка функции в которой измеряется длина изначального варианта и конечного результата."""
    masked_number = get_mask_card_number(simple_card_number)
    assert len(simple_card_number) == correct_len_card_number
    assert len(masked_number) == len(masked_card_number)


def test_get_mask_account(masked_card_account: str) -> None:
    """Проверка функциональности mask_account"""
    assert get_mask_account("1234123412341234") == masked_card_account


@pytest.mark.parametrize(
    "card_number, expection",
    [
        ("1111222233334444123", ValueError),  # Ошибка длины
        ("AAAABBBBCCCCDDDD", ValueError),  # Ошибка с использованием букв
        ("123!123!123!", ValueError),  # Ошибка с использованием символов
        ("", ValueError),
        (" ", ValueError),
    ],
)
def test_get_mask_account_value_error(card_number: str, expection: type[Exception]) -> None:
    """Проверка ошибочных данных в mask_account"""
    with pytest.raises(expection):
        get_mask_account(card_number)


def test_get_mask_account_len(masked_card_account: str, simple_card_number: str) -> None:
    masked_account = get_mask_account(simple_card_number)
    assert len(masked_account) == len(masked_card_account)

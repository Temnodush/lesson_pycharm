import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card",
    [
        "Счёт 1234123412341234",  # Ошибка с использованием символов.
        "MasterCard 1111222233334444",
        "СЧЕТ 1111222233334444",  # Ошибка с использованием букв.
        "MIR 1234123412341234",
    ],
)
def test_mask_account_card(account_card: str) -> None:
    """Проверка работы функции mask_account_card"""
    assert mask_account_card(account_card)


@pytest.mark.parametrize(
    "account_card, exception",
    [
        ("Счёт 123412341234123!", ValueError),  # Ошибка с использованием символов.
        ("MasterCard 11112222333344445555", ValueError),  # Ошибка длины.
        ("123 abcdefghijklmnop", ValueError),  # Ошибка с использованием букв.
        ("", ValueError),
        (" ", ValueError),
    ],
)
def test_mask_account_card_invalid(account_card: str, exception: type[Exception]) -> None:
    """Проверка ошибочных аргумнентов в masc_account_card"""
    with pytest.raises(exception):
        mask_account_card(account_card)


def test_get_date(standard_date: str) -> None:
    """Проверка работы функции test_get_date"""
    assert get_date(standard_date)


# 2024-03-11T02:26:18.671407


@pytest.mark.parametrize(
    "incorrect_date, exception",
    [
        ("123456789123456ASDASD", ValueError),  # Ошибка с использованием символов.
        ("MasterCard 11112222333344445555", ValueError),  # Ошибка длины.
        ("123 abcdefghijklmnop", ValueError),  # Ошибка с использованием букв.
        ("", ValueError),
        (" ", ValueError),
        (None, ValueError),
    ],
)
def test_get_date_incorrect(incorrect_date: str, exception: type[Exception]) -> None:
    """Проверка ошибочных аргументов функции get_date"""
    with pytest.raises(exception):
        get_date(incorrect_date)

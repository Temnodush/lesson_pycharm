import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(masked_card_number):
    """Проверяет корректность маскирования номера карты в формате XXXXXX******XXXX."""
    assert get_mask_card_number("1234567890123456") == masked_card_number


@pytest.mark.parametrize(
    "card_number, exception",
    [
        ("123412341234123!", ValueError),
        ("11112222333344445555", ValueError),
        ("abcdefghijklmnop", ValueError),
        ("", ValueError),
        (" ", ValueError),
    ],
)
def test_get_mask_card_number_value_error(card_number, exception):
    """Проверяет обработку невалидных номеров карт (спецсимволы, длина, буквы)."""
    with pytest.raises(exception):
        get_mask_card_number(card_number)


def test_get_mask_card_len(simple_card_number, masked_card_number):
    """Проверяет сохранение длины номера карты после маскирования."""
    masked = get_mask_card_number(simple_card_number)
    assert len(simple_card_number) == 16
    assert len(masked) == len(masked_card_number)


def test_get_mask_account(masked_card_account, simple_account_number):
    """Проверяет корректность маскирования номера счета в формате **XXXX."""
    assert get_mask_account(simple_account_number) == masked_card_account


@pytest.mark.parametrize(
    "account_number, exception",
    [
        ("1111222233334444123", ValueError),
        ("AAAABBBBCCCCDDDD", ValueError),
        ("123!123!123!", ValueError),
        ("", ValueError),
        (" ", ValueError),
    ],
)
def test_get_mask_account_value_error(account_number, exception):
    """Проверяет обработку невалидных номеров счетов (длина, спецсимволы, буквы)."""
    with pytest.raises(exception):
        get_mask_account(account_number)


def test_get_mask_account_len(masked_card_account, simple_account_number):
    """Проверяет сохранение длины номера счета после маскирования."""
    masked = get_mask_account(simple_account_number)
    assert len(masked) == len(masked_card_account)

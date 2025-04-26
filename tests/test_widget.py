import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("card, expected", [
    ("Visa Classic 1234567890123456", "Visa Classic 1234 56** **** 3456"),
    ("Mastercard 9876543210987654", "Mastercard 9876 54** **** 7654"),
    ("Счет 12345678901234567890", "Счет **7890"),
    ("", "Неверный формат номера"),
    ("Невалидный номер", "Неверный формат номера")
])
def test_mask_account_card(card, expected):
    """Проверяет корректность маскирования различных форматов карт и счетов."""
    assert mask_account_card(card) == expected

@pytest.mark.parametrize("date_str, expected", [
    ("2023-10-26T00:00:00", "26.10.2023"),
    ("2024-01-01T12:00:00", "01.01.2024")
])
def test_get_date_valid(date_str, expected):
    """Проверяет преобразование валидных дат в DD.MM.YYYY."""
    assert get_date(date_str) == expected

@pytest.mark.parametrize("invalid_date", [
    "",
    "26.10.2023T00:00:00",
    "2023-10-26"
])
def test_get_date_invalid(invalid_date):
    """Проверяет обработку невалидных форматов даты (вызов исключения)."""
    with pytest.raises(ValueError):
        get_date(invalid_date)
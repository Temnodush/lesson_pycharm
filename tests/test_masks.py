from src.masks import get_mask_card_number, get_mask_account
import pytest

@pytest.mark.parametrize("card_number, exception",
                         [
                         ("123412341234123!", ValueError), # Ошибка с использованием символов.
                         ("11112222333344445555", ValueError), # Ошибка длины.
                         ("abcdefghijklmnop", ValueError) # Ошибка с использованием букв.
                         ])
def test_mask_card_number_value_error(card_number, exception):
    """Проверка функции с ошибками ValueError"""
    with pytest.raises(exception):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number, expected",
                          [
                          ("1234123412341234", "1234 12** **** 1234"), # Проверка работоспособности.
                          ("1111222233334444", "1111 22** **** 4444"), # Проверка работоспособности.
                          ("5555222211113333", "5555 22** **** 3333") # Проверка работоспособности.
                          ])
def test_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number, exception",
                         [
                             ("1111222233334444", "XX4444"),
                             ("2222222222222222", "XX2222"),
                             ("0000000000000000", "XX0000")
                         ])
def test_get_mask_account(card_number, exception):
    assert get_mask_account(card_number) == exception

@pytest.mark.parametrize("card_number, expection",
                         [("1111222233334444123", ValueError), # Ошибка длины
                          ("AAAABBBBCCCCDDDD", ValueError), # Ошибка с использованием букв
                          ("123!123!123!", ValueError) # Ошибка с использованием символов
                          ])
def test_get_mask_account_value_error(card_number, expection):
    with pytest.raises(expection):
       get_mask_account(card_number)
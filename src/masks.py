def get_mask_card_number(card_number: str) -> str:
    """Функция, которая позволяет шифровать номер карты в формате "1234 12** **** 1234" """
    if not card_number.strip():
        raise ValueError("Необходимо ввести номер")
    if len(card_number) != 16:
        raise ValueError("Карта должна состоять ровно из 16 цифр.")
    if not card_number.isdigit():
        raise ValueError("Номер должен состоять только из цифр.")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(card_number: str) -> str:
    """Функция, которая выводит 4 последние цифры карты и шифрует две предыдущие."""
    if card_number == "" or card_number == " ":
        raise ValueError("Необходимо ввести номер")
    elif len(card_number) != 16:
        raise ValueError("Карта должна состоять ровно из 16 цифр.")
    elif not card_number.isdigit():
        raise ValueError("Номер должен состоять только из цифр.")
    return f"XX{card_number[12:]}"

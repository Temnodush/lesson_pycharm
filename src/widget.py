from .masks import get_mask_account, get_mask_card_number

def mask_account_card(card: str) -> str:
    """Обрабатывает и маскирует номер карты или счета в зависимости от длины номера."""
    numbers = ""
    name = ""
    for char in card:
        if char.isdigit():
            numbers += char
        elif char.isalpha() or char.isspace():
            name += char
    name = name.strip()
    if len(numbers) == 16:
        return f"{name} {get_mask_card_number(numbers)}" if name else get_mask_card_number(numbers)
    elif len(numbers) == 20:
        return f"{name} {get_mask_account(numbers)}" if name else get_mask_account(numbers)
    return "Неверный формат номера"

def get_date(date_str: str) -> str:
    """Функция принимает строку с датой и возвращает часть содержимого в нужной последовательности."""
    if not date_str:
        raise ValueError("Дата не может быть пустой строкой.")
    if "T" not in date_str:
        raise ValueError("Некорректный формат даты.")
    date_part = date_str.split("T")[0]
    parts = date_part.split("-")
    if len(parts) != 3:
        raise ValueError("Некорректный формат даты.")
    return f"{parts[2]}.{parts[1]}.{parts[0]}"
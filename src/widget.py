def mask_account_card(card: str) -> str:
    """Функция принимает счёт или карту и шифрует в зависимости от содержимого."""
    numbers = ""
    for number in card:
        if number.isdigit():
            numbers += number
    if len(numbers) != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр.")
    if card[:4].lower() == "счет" or card[:4].lower() == "счёт":
        mask = f"**{numbers[12:]}"
    else:
        mask = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[12:]}"
    return mask


def get_date(date: str) -> str:
    """Принимает дату и приводит её к новому формату."""
    if date == None:
        raise ValueError("Произошла ошибка! Дата отсутствует.")
    new_date = ""
    for i in date:
        if i.isdigit() and len(new_date) < 8:
            new_date += i
    if len(new_date) != 8:
        raise ValueError("Не удалось извлечь дату в формате YYYYMMDD")
    date_year = new_date[:4]
    date_month = new_date[4:6]
    date_day = new_date[6:]
    if not 2000 < int(date_year) <= 2025:
        raise ValueError("Год указан некорректно.")
    if not 1 <= int(date_month) <= 12:
        raise ValueError("Месяц указан некорректно.")
    if not 1 <= int(date_day) <= 31:
        raise ValueError("День указан некорректно.")
    return f"{date_day}.{date_month}.{date_year}"

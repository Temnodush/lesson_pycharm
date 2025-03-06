def mask_account_card(card: str) -> str:
    """Функция принимает счёт или карту и шифрует в зависимости от содержимого."""
    numbers = ""
    for number in card:
        if number.isdigit():
            numbers += number
    if card[:4].lower() == "счет":
        mask = f"**{numbers[12:]}"
    else:
        mask = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[12:]}"
    return mask


def get_date(date: str) -> str:
    """Функция принимает строку с датой и возвращает часть содержимого в нужной последовательности."""
    full_date = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    return full_date


user_card = "Visa Platinum 7000792289606361"
print(mask_account_card(user_card))
#datatime = "2024-03-11T02:26:18.671407"
#print(get_date(datatime))


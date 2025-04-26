from config import PATH_TO_CSV, PATH_TO_EXCEL, PATH_TO_JSON
from src.filters import filter_description
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.transactions_read import read_csv_transactions, read_excel_transactions
from src.utils import read_json_transactions
from src.widget import get_date, mask_account_card


def choose_file_format():
    print(
        "Привет! Добро пожаловать в программу работы\n"
        "с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )
    while True:
        choose_file = input("> ")
        if choose_file == "1":
            print("Для обработки выбран JSON-файл.")
            return "JSON"
        elif choose_file == "2":
            print("Для обработки выбран CSV-файл.")
            return "CSV"
        elif choose_file == "3":
            print("Для обработки выбран XLSX-файл.")
            return "XLSX"
        else:
            print("Введено некорректное значение.")
            continue


def status_filter():
    print(
        """
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING."""
    )
    while True:
        change_status = input().upper()
        states = ["EXECUTED", "CANCELED", "PENDING"]
        if change_status in states:
            print(f"Операции отфильтрованы по статусу {change_status}")
            return change_status.upper()
        else:
            print(f'Статус операции "{change_status}" недоступен.')
            continue


def sorted_by_date():
    print("Отсортировать операции по дате? Да/Нет")
    while True:
        sorted_date = input().upper()
        if sorted_date == "ДА":
            print("Отсортировать по возрастанию или по убыванию?")
            while True:
                sort_by_order = input().upper()
                if sort_by_order == "ПО УБЫВАНИЮ":
                    return "Y", "DECREASING"
                elif sort_by_order == "ПО ВОЗРАСТАНИЮ":
                    return "Y", "INCREASING"
                else:
                    print("Введено некорректное значение.")
                    continue
        elif sorted_date == "НЕТ":
            return "N", False
        else:
            print("Введено некорректное значение.")
            continue


def filter_by_rub():
    print("Выводить только рублевые транзакции? Да/Нет")
    while True:
        change_filter_rub_currency = input().upper()
        if change_filter_rub_currency == "ДА":
            return "Y"
        elif change_filter_rub_currency == "НЕТ":
            return "N"
        else:
            print("Введено некорректное значение.")
            continue


def search_status():
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    while True:
        description_search = input().upper()
        if description_search == "ДА":
            return "Y"
        elif description_search == "НЕТ":
            return "N"
        else:
            print("Введено некорректное значение.")
            continue


def filter_activated(choose_file, status, by_date, by_rub, description_search):
    transactions = []
    if choose_file == "JSON":
        transactions = read_json_transactions(PATH_TO_JSON)
    elif choose_file == "CSV":
        transactions = read_csv_transactions(PATH_TO_CSV)
    elif choose_file == "XLSX":
        transactions = read_excel_transactions(PATH_TO_EXCEL)

    transactions = filter_by_state(transactions, status)

    if by_date[0] == "Y":
        reverse = by_date[1] == "DECREASING"
        transactions = sort_by_date(transactions, reverse)

    if by_rub == "Y":
        transactions = list(filter_by_currency(transactions, "RUB"))

    if description_search == "Y":
        search_word = input("Введите ключевое слово для поиска: ").lower()
        transactions = list(filter_description(transactions, search_word))

    return transactions


def main():
    choose_file = choose_file_format()
    change_status = status_filter()
    sorted_date = sorted_by_date()
    filter_rub = filter_by_rub()
    description_search = search_status()
    transactions = filter_activated(choose_file, change_status, sorted_date, filter_rub, description_search)
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке {len(transactions)}")

    for transaction in transactions:
        date = get_date(transaction.get("date", "Дата неизвестна"))
        description = transaction.get("description", "Описание отсутствует")

        from_data = str(transaction.get("from", "")).strip()
        to_data = str(transaction.get("to", "")).strip()

        from_account = mask_account_card(from_data) if from_data != "nan" else "Нет данных"
        to_account = mask_account_card(to_data) if to_data != "nan" else "Нет данных"

        if from_account not in ("Неверный формат номера", "Нет данных"):
            direction = f"{from_account} -> {to_account}"
        else:
            direction = to_account

        operation_amount = transaction.get("operationAmount", {})
        amount = operation_amount.get("amount", "Сумма не указана")
        currency_code = operation_amount.get("currency", {}).get("code", "Валюта не указана")

        print(
            f"""
    Дата: {date} {description}
    {direction}
    Сумма: {amount} {currency_code}
                """.strip()
        )


if __name__ == "__main__":
    main()

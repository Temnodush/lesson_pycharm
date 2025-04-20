import os

import pandas as pd

current_file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(current_file_path)
project_root = os.path.dirname(src_dir)
data_dir = os.path.join(project_root, "data")
file_path_csv = os.path.join(data_dir, "transactions.csv")
file_path_xlsx = os.path.join(data_dir, "transactions_excel.xlsx")


def read_csv_transactions(filepath):
    """Функция читает транзакции из CSV-файла и возвращает их в виде списка словарей"""
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Файл {filepath} не найден")
        df = pd.read_csv(filepath, sep=";")
        data = df.to_dict("records")
        return [row for row in data]
    except FileNotFoundError as e:
        print(f"Ошибка! Файл не найден.: {e}")
        return []
    except Exception as e:
        print(f"Неизвестная ошибка! {str(e)}")
        return []


def read_excel_transactions(filepath):
    """Функция читает транзакции из XLSX-файла и возвращает их в виде списка словарей"""
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Файл {filepath} не найден")
        df = pd.read_excel(filepath)
        data = df.to_dict("records")
        return [row for row in data]
    except FileNotFoundError as e:
        print(f"Ошибка! Файл не найден.: {e}")
        return []
    except Exception as e:
        print(f"Неизвестная ошибка! {str(e)}")
        return []


print(read_excel_transactions(file_path_xlsx))

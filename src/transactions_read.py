import csv
import os

import pandas as pd

current_file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(current_file_path)
project_root = os.path.dirname(src_dir)
data_dir = os.path.join(project_root, "data")
file_path_csv = os.path.join(data_dir, "transactions.csv")
file_path_xlsx = os.path.join(data_dir, "transactions_excel.xlsx")


def read_csv_transactions(path):
    """Функция читает транзакции из CSV-файла и возвращает их в виде списка словарей."""
    transactions = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                transaction = {
                    "id": row.get("id", ""),
                    "state": row.get("state", ""),
                    "date": row.get("date", ""),
                    "operationAmount": {
                        "amount": row.get("amount", ""),
                        "currency": {"name": row.get("currency_name", ""), "code": row.get("currency_code", "")},
                    },
                    "from": str(row.get("from", "")).strip() or "Нет данных",
                    "to": str(row.get("to", "")).strip() or "Нет данных",
                    "description": row.get("description", ""),
                }
                transactions.append(transaction)
        return transactions
    except FileNotFoundError:
        print(f"Файл не найден по пути: {path}")
        return []
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return []


def read_excel_transactions(filepath):
    """Функция читает транзакции из XLSX-файла и возвращает их в виде списка словарей"""
    try:
        df = pd.read_excel(filepath)
        transaction_list = []
        for _, row in df.iterrows():
            transaction = {
                "id": row.get("id"),
                "state": row.get("state"),
                "date": row.get("date"),
                "operationAmount": {
                    "amount": row.get("amount"),
                    "currency": {"name": row.get("currency_name"), "code": row.get("currency_code")},
                },
                "description": row.get("description"),
                "from": row.get("from"),
                "to": row.get("to"),
            }
            transaction_list.append(transaction)

        return transaction_list
    except FileNotFoundError:
        print(f"Файл не найден по пути: {filepath}")
        return []
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return []

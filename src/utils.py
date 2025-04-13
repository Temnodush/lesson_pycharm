import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "../data/operations.json")


def read_file(filename=None):
    """Функция чтения файла с транзакциями."""
    if filename is None:
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []

        return data
    except FileNotFoundError:
        print(f"Файл не найден по пути: {filename}")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка при декодировании JSON из файла: {filename}")
        return []

import json
import logging
import os
from pathlib import Path

file_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = Path(file_dir).parent / "logs"
log_dir.mkdir(parents=True, exist_ok=True)
file_path = log_dir / "utils.log"

# Настройка file_formatter
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

# Настройка file_handler
file_handler = logging.FileHandler(file_path, mode="w", encoding="utf-8")
file_handler.setFormatter(file_formatter)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)


def read_file(filename=None):
    """Функция чтения файла с транзакциями."""
    if filename is None:
        logger.error("Читаемый файл не указан.")
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.debug("Файл найден.")

        if not isinstance(data, list):
            logger.error("Содержимое файла не является списком.")
            return []
        logger.info("Файл прочтён.")
        return data
    except FileNotFoundError:
        logger.error("Файл не найден.")
        print(f"Файл не найден по пути: {filename}")
        return []
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования.")
        print(f"Ошибка при декодировании JSON из файла: {filename}")
        return []

import logging
import os
from pathlib import Path

file_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = Path(file_dir).parent / "logs"
log_dir.mkdir(parents=True, exist_ok=True)
file_path = log_dir / "masks.log"

# Настройка file_formatter
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

# Настройка file_handler
file_handler = logging.FileHandler(file_path, mode="w", encoding="utf-8")
file_handler.setFormatter(file_formatter)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая позволяет шифровать номер карты в формате "1234 12** **** 1234" """
    if not card_number.strip():
        logger.error("Пользователь ввёл некорректное значение.")
        raise ValueError("Необходимо ввести номер")
    if len(card_number) != 16:
        logger.error("Пользователь ввёл некорректную длину номера карты.")
        raise ValueError("Карта должна состоять ровно из 16 цифр.")
    if not card_number.isdigit():
        logger.error("Пользователь ввёл не цифровое значение.")
        raise ValueError("Номер должен состоять только из цифр.")
    logger.info("Номер карты успешно зашифрован.")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(card_number: str) -> str:
    """Функция, которая выводит 4 последние цифры карты и шифрует две предыдущие."""
    if card_number == "" or card_number == " ":
        logger.error("Пользователь ввёл некорректное значение.")
        raise ValueError("Необходимо ввести номер")
    elif len(card_number) != 16:
        logger.error("Пользователь ввёл некорректную длину номера карты.")
        raise ValueError("Карта должна состоять ровно из 16 цифр.")
    elif not card_number.isdigit():
        logger.error("Пользователь ввёл не цифровое значение.")
        raise ValueError("Номер должен состоять только из цифр.")
    logger.info("Номер карты успешно зашифрован.")
    return f"XX{card_number[12:]}"

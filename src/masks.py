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
    """Маскирует номер карты в формате 'XXXX XX** **** XXXX' (16 цифр)."""
    if not card_number.strip():
        logger.error("Пустой номер карты.")
        raise ValueError("Необходимо ввести номер")
    if len(card_number) != 16 or not card_number.isdigit():
        logger.error("Неверный формат номера карты.")
        raise ValueError("Карта должна содержать 16 цифр")
    logger.info("Номер карты зашифрован.")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета в формате '**XXXX' (последние 4 цифры из 20)."""
    if not account_number.strip():
        logger.error("Пустой номер счета.")
        raise ValueError("Необходимо ввести номер")
    if len(account_number) != 20 or not account_number.isdigit():
        logger.error("Неверный формат номера счета.")
        raise ValueError("Счет должен содержать 20 цифр")
    logger.info("Номер счета зашифрован.")
    return f"**{account_number[-4:]}"

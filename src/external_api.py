import os
from typing import Any

import requests
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY не найден в .env")


def convert_amount(transaction) -> float | None | Any:
    """Функция конвертация валюты в RUB"""
    amount_data = transaction["operationAmount"]
    amount = float(amount_data["amount"])
    currency = amount_data["currency"]["code"]
    if amount == 0:
        return amount
    elif currency != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": API_KEY}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            result = response.json()
            return round(result["result"], 2)
        except Exception as e:
            raise RuntimeError(f"Ошибка конвертации: {e}")
    else:
        return amount


transactions_finance = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "100", "currency": {"code": "USD"}},
}

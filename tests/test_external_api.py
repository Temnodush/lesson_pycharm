from unittest.mock import Mock, patch

import pytest
import requests

from src.external_api import convert_amount


@patch("requests.get")
def test_convert_rub_currency(mock_get):
    """Тест с конвертацией RUB в RUB"""
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}}
    result = convert_amount(transaction)
    assert result == 100.0
    mock_get.assert_not_called()


def test_zero_amount():
    """Тест суммы равное нулю (граничное значение)"""
    transaction = {"operationAmount": {"amount": "0", "currency": {"code": "USD"}}}
    assert convert_amount(transaction) == 0.0


@patch("requests.get")
def test_api_error_response(mock_get):
    """Тест обработки HTTP-ошибки"""
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.HTTPError("Not Found")
    mock_get.return_value = mock_response
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "EUR"}}}
    with pytest.raises(RuntimeError) as exc_info:
        convert_amount(transaction)
    assert "Ошибка конвертации" in str(exc_info.value)


@patch("requests.get")
def test_conversion_error(mock_get):
    """Тест обработки ошибки при конвертации"""
    mock_get.side_effect = requests.exceptions.RequestException("API Error")

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "EUR"}}}

    with pytest.raises(RuntimeError, match="Ошибка конвертации: API Error"):
        convert_amount(transaction)

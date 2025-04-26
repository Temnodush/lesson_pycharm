from unittest.mock import Mock, patch, mock_open
import pandas as pd
from src.transactions_read import read_csv_transactions, read_excel_transactions


@patch("builtins.open", new_callable=mock_open, read_data=(
        "id;state;date;amount;currency_name;currency_code;description;from;to\n"
        "1;EXECUTED;2023-01-01;100;RUB;RUB;Payment;Account 1 ;Account2\n"
        "2;PENDING;2023-01-02;200;USD;USD;Transfer;;Account4\n"
))
def test_read_csv_transactions_success(mock_file):
    """Проверяет корректное чтение и парсинг CSV-файла с транзакциями."""
    result = read_csv_transactions("fake.csv")
    assert len(result) == 2
    mock_file.assert_called_once_with("fake.csv", "r", encoding="utf-8")


@patch("builtins.open")
def test_read_csv_transactions_file_not_found(mock_open):
    """Проверяет обработку отсутствия CSV-файла (возврат пустого списка)."""
    mock_open.side_effect = FileNotFoundError
    result = read_csv_transactions("missing.csv")
    assert result == []
    mock_open.assert_called_once()


@patch("builtins.open")
def test_read_csv_transactions_general_error(mock_open):
    """Проверяет обработку общих ошибок при чтении CSV (возврат пустого списка)."""
    mock_open.side_effect = Exception("Error")
    result = read_csv_transactions("error.csv")
    assert result == []
    mock_open.assert_called_once()


# Тесты для Excel
@patch("pandas.read_excel")
def test_read_excel_transactions_success(mock_read_excel):
    """Проверяет корректное чтение и преобразование данных из Excel-файла."""
    mock_df = Mock(spec=pd.DataFrame)
    mock_df.iterrows.return_value = [(0, {"id": 1, "amount": 100})]
    mock_read_excel.return_value = mock_df

    result = read_excel_transactions("fake.xlsx")
    assert len(result) == 1
    mock_read_excel.assert_called_once_with("fake.xlsx")


@patch("pandas.read_excel")
def test_read_excel_transactions_file_not_found(mock_read_excel):
    """Проверяет обработку отсутствия Excel-файла (возврат пустого списка)."""
    mock_read_excel.side_effect = FileNotFoundError
    result = read_excel_transactions("missing.xlsx")
    assert result == []
    mock_read_excel.assert_called_once()


@patch("pandas.read_excel")
def test_read_excel_transactions_general_error(mock_read_excel):
    """Проверяет обработку общих ошибок при чтении Excel (возврат пустого списка)."""
    mock_read_excel.side_effect = Exception("Error")
    result = read_excel_transactions("error.xlsx")
    assert result == []
    mock_read_excel.assert_called_once()
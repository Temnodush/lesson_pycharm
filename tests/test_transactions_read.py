from unittest.mock import patch, Mock
from src.transactions_read import read_csv_transactions, read_excel_transactions


@patch('src.transactions_read.pd.read_csv')
@patch('src.transactions_read.os.path.exists')
def test_read_csv_transactions(mock_exists, mock_read_csv):
    """Тест успешного прочтения CSV файла."""
    mock_exists.return_value = True
    mock_df = Mock()
    mock_data = [{'id': 1, 'state': 'EXECUTED'}, {'id': 2, 'state': 'PENDING'}]
    mock_df.to_dict.return_value = mock_data
    mock_read_csv.return_value = mock_df
    result = read_csv_transactions('test.csv')

    mock_exists.assert_called_once_with('test.csv')
    mock_read_csv.assert_called_once_with('test.csv', sep=';')
    assert result == mock_data


@patch('src.transactions_read.os.path.exists')
def test_read_csv_not_found(mock_exists):
    """Тест обработки отсутствующего CSV файла."""
    mock_exists.return_value = False
    with patch('src.transactions_read.print') as mock_print:
        result = read_csv_transactions('missing.csv')
        mock_print.assert_called_once_with('Ошибка! Файл не найден.: Файл missing.csv не найден')
        assert result == []


@patch('src.transactions_read.pd.read_csv')
@patch('src.transactions_read.os.path.exists')
def test_read_csv_error(mock_exists, mock_read_csv):
    """Тест обработки ошибки чтения CSV файла"""
    mock_exists.return_value = True
    mock_read_csv.side_effect = Exception("Test error")
    with patch('src.transactions_read.print') as mock_print:
        result = read_csv_transactions('corrupted.csv')
        mock_print.assert_called_once_with('Неизвестная ошибка! Test error')
        assert result == []


@patch('src.transactions_read.pd.read_excel')
@patch('src.transactions_read.os.path.exists')
def test_read_excel_success(mock_exists, mock_read_excel):
    """Тест успешного чтения XLSX файла"""
    mock_exists.return_value = True
    mock_df = Mock()
    mock_data = [{'id': 100, 'amount': 500}, {'id': 200, 'amount': 1000}]
    mock_df.to_dict.return_value = mock_data
    mock_read_excel.return_value = mock_df
    result = read_excel_transactions('test.xlsx')
    mock_exists.assert_called_once_with('test.xlsx')
    mock_read_excel.assert_called_once_with('test.xlsx')
    assert result == mock_data


@patch('src.transactions_read.pd.read_excel')
@patch('src.transactions_read.os.path.exists')
def test_read_excel_error(mock_exists, mock_read_excel):
    """Тест обработки ошибки XLSX файла"""
    mock_exists.return_value = True
    mock_read_excel.side_effect = Exception("Excel error")
    with patch('src.transactions_read.print') as mock_print:
        result = read_excel_transactions('corrupted.xlsx')
        mock_print.assert_called_once_with('Неизвестная ошибка! Excel error')
        assert result == []
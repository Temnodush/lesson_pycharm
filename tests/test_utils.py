import json
from unittest.mock import mock_open, patch

from src.utils import read_file


@patch("json.load")
@patch("builtins.open")
def test_read_valid_json_list(mock_open_func, mock_json_load):
    """Тест корректного чтения валидного JSON-списка"""
    test_data = [{"test": "data"}, 123, "value"]
    mock_json_load.return_value = test_data
    mock_open_func.return_value = mock_open(read_data=json.dumps(test_data)).return_value

    result = read_file("dummy_path.json")

    mock_open_func.assert_called_once_with("dummy_path.json", "r", encoding="utf-8")
    mock_json_load.assert_called_once()
    assert result == test_data


def test_read_valid_json_not_list(tmpdir, capsys):
    """Тест чтения JSON, который не является списком"""
    data = {"key": "value"}
    file = tmpdir.join("test.json")
    file.write(json.dumps(data))

    result = read_file(file.strpath)
    captured = capsys.readouterr()

    assert result == []
    assert captured.out == ""


def test_read_nonexistent_file(capsys):
    """Тест обработки отсутствующего файла"""
    result = read_file("non_existent_file.json")
    captured = capsys.readouterr()

    assert result == []
    assert "Файл не найден по пути: non_existent_file.json" in captured.out


def test_default_filename():
    """Тест поведения при отсутствии имени файла"""
    result = read_file()
    assert result == []


@patch("builtins.open")
def test_read_file_not_found(mock_open):
    """Тест возвращает пустой список при отсутствии файла"""
    mock_open.side_effect = FileNotFoundError
    result = read_file("nonexistent.json")
    assert result == []

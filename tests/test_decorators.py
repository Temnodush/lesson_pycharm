import pytest

from src.decorators import log


def test_log_success_with_file(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def add(a, b):
        return a + b

    assert add(2, 3) == 5
    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert "add started ok" in content
    assert "finished with result: 5" in content


def test_log_success_without_filename(capsys):
    @log()
    def subtract(a, b):
        return a - b

    assert subtract(5, 3) == 2
    captured = capsys.readouterr()
    assert "subtract started ok" in captured.out
    assert "finished with result: 2" in captured.out


def test_log_exception_with_file(tmp_path):
    log_file = tmp_path / "error_log.txt"

    @log(filename=str(log_file))
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    content = log_file.read_text(encoding="utf-8")
    assert "divide ошибка: ZeroDivisionError" in content
    assert "Inputs: (10, 0), {}" in content


def test_log_preserves_function_identity():
    @log("my_log.txt")
    def sample():
        """Тестовая функция"""
        pass

    assert sample.__name__ == "sample"
    assert sample.__doc__ == "Тестовая функция"

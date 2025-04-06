import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_simple_test(simple_transactions: list[dict]) -> None:
    """Проверка работы функции filter_by_state"""
    assert filter_by_state(simple_transactions)


def test_filter_by_state_missing_key(transactions_without_state: list[dict]) -> None:
    """Проверка некорректных значений функции filter_by_state"""
    with pytest.raises(KeyError):
        filter_by_state(transactions_without_state)


@pytest.mark.parametrize(
    "state",
    [
        "EXECUTED",
        "CANCELED",
    ],
)
def test_filter_by_state_with_params(simple_transactions: list[dict], state: str) -> None:
    """Проверка корректных значений state."""
    result = filter_by_state(simple_transactions, state)
    assert [t["id"] for t in result]


def test_sort_by_date(simple_transactions: list[dict]) -> None:
    """Проверка функции sort_by_date"""
    assert sort_by_date(simple_transactions)

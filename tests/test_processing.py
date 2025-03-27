from src.processing import filter_by_state, sort_by_date
import pytest


def test_filter_by_state_simple_test(simple_transactions):
    assert filter_by_state(simple_transactions)


def test_filter_by_state_missing_key(transactions_without_state):
    with pytest.raises(KeyError):
        filter_by_state(transactions_without_state)


@pytest.mark.parametrize("state", [
    "EXECUTED",
    "CANCELED",
])
def test_filter_by_state_with_params(simple_transactions, state):
    result = filter_by_state(simple_transactions, state)
    assert [t["id"] for t in result]


def test_sort_by_date(simple_transactions):
    assert sort_by_date(simple_transactions)
import pytest


@pytest.fixture
def masked_card_number() -> str:
    return "1234 12** **** 1234"


@pytest.fixture
def correct_len_card_number() -> int:
    return 16


@pytest.fixture
def simple_card_number() -> str:
    return "1234123412341234"


@pytest.fixture
def masked_card_account() -> str:
    return "XX1234"


@pytest.fixture
def standard_date() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def simple_transactions() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def transactions_without_state() -> list[dict]:
    return [
        {"id": 1, "date": "2023-01-15T12:30:00.000000"},
        {"id": 2, "date": "2023-01-14T11:20:00.000000"},
    ]

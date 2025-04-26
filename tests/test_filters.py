from src.filters import count_transactions_by_category, filter_description


def test_filter_description_found(simple_transactions):
    """Проверяет корректность фильтрации транзакций по наличию ключевой фразы в описании."""
    search_str = "Перевод организации"
    result = filter_description(simple_transactions, search_str)
    assert len(result) == 2
    for transaction in result:
        assert "Перевод организации" in transaction["description"]


def test_filter_description_case_insensitive(simple_transactions):
    """Проверяет регистронезависимость поиска при фильтрации по описанию транзакций."""
    search_str = "пЕревОд ОргАнизации"
    result = filter_description(simple_transactions, search_str)
    assert len(result) == 2


def test_filter_description_not_found(simple_transactions):
    """Проверяет обработку случая, когда поисковый запрос не найден в описаниях."""
    search_str = "Отсутствующий текст"
    result = filter_description(simple_transactions, search_str)
    assert len(result) == 0


def test_filter_description_empty_transactions():
    """Проверяет обработку пустого списка транзакций при фильтрации по описанию."""
    transactions = []
    result = filter_description(transactions, "test")
    assert result == []


def test_filter_description_empty_search_string(simple_transactions):
    """Проверяет фильтрацию с пустой строкой поиска."""
    result = filter_description(simple_transactions, "")
    expected_count = sum(1 for t in simple_transactions if t.get("description"))
    assert len(result) == expected_count


def test_count_by_category_sample_data(simple_transactions, sample_categories):
    """Проверяет корректность подсчета транзакций по категориям на тестовых данных."""
    result = count_transactions_by_category(simple_transactions, sample_categories)
    expected = {
        "Переводы организациям": 2,
        "Межсчетовые переводы": 2,
        "Вклады": 0,
        "Межкартовые переводы": 2,
        "Пополнение счета с карты": 0,
    }
    assert result == expected


def test_count_by_category_empty_transactions(sample_categories):
    """Проверяет подсчет транзакций по категориям при пустом списке транзакций."""
    result = count_transactions_by_category([], sample_categories)
    expected = {cat: 0 for cat in sample_categories}
    assert result == expected


def test_count_by_category_case_insensitive():
    """Проверяет регистронезависимость при сопоставлении транзакций с категориями."""
    transactions = [{"description": "перевод организации"}]
    categories = {"TestCategory": ["ПЕРЕВОД ОРГАНИЗАЦИИ"]}
    result = count_transactions_by_category(transactions, categories)
    assert result["TestCategory"] == 1


def test_count_by_category_multiple_keywords():
    """Проверяет подсчет транзакций по категории с несколькими ключевыми словами."""
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Оплата услуг"},
        {"description": "Покупка"},
    ]
    categories = {"TestCategory": ["организации", "услуг", "покупка"]}
    result = count_transactions_by_category(transactions, categories)
    assert result["TestCategory"] == 3

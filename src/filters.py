import re
from collections import Counter
from typing import List, Any, Dict


def filter_description(transactions: List[Dict[str, Any]], search_string):
    """Фильтрует транзакции по наличию ключевого слова в описании."""
    result = []
    pattern = re.compile(search_string, re.IGNORECASE)
    for transaction in transactions:
        description = transaction.get("description", "")
        if description and pattern.search(description):
            result.append(transaction)
    return result


def count_transactions_by_category(
    transactions: List[Dict[str, Any]], categories: Dict[str, List[str]]
) -> Dict[str, int]:
    """Считает количество транзакций по категориям на основе ключевых слов в описании."""
    matched_categories = []
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category, keywords in categories.items():
            if any(keyword.lower() in description for keyword in keywords):
                matched_categories.append(category)
    category_counter = Counter(matched_categories)
    return {category: category_counter.get(category, 0) for category in categories}

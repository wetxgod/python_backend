import pytest
from tracker import FinanceTracker


def test_new_tracker_has_zero_balance():
    tracker = FinanceTracker()

    assert tracker.get_total_income() == 0
    assert tracker.get_total_expense() == 0
    assert tracker.calculate_balance() == 0


def test_add_income():
    tracker = FinanceTracker()

    tracker.add_income(50000)

    assert tracker.get_total_income() == 50000
    assert tracker.get_income_count() == 1
    assert tracker.calculate_balance() == 50000


def test_add_expense():
    tracker = FinanceTracker()

    tracker.add_expense(10000)

    assert tracker.get_total_expense() == 10000
    assert tracker.get_expense_count() == 1
    assert tracker.calculate_balance() == -10000


def test_calculate_balance():
    tracker = FinanceTracker()

    tracker.add_income(50000)
    tracker.add_income(30000)
    tracker.add_expense(10000)

    assert tracker.calculate_balance() == 70000


def test_zero_income_raises_error():
    tracker = FinanceTracker()

    with pytest.raises(ValueError):
        tracker.add_income(0)


def test_negative_expense_raises_error():
    tracker = FinanceTracker()

    with pytest.raises(ValueError):
        tracker.add_expense(-1000)


def test_invalid_amount_error_message():
    tracker = FinanceTracker()

    with pytest.raises(
        ValueError,
        match="Amount must be greater than zero.",
    ):
        tracker.add_income(-500)


def test_clear_data():
    tracker = FinanceTracker()

    tracker.add_income(50000)
    tracker.add_expense(10000)
    tracker.clear_data()

    assert tracker.get_incomes() == []
    assert tracker.get_expenses() == []
    assert tracker.calculate_balance() == 0


def test_get_statistics():
    tracker = FinanceTracker()

    tracker.add_income(50000)
    tracker.add_income(30000)
    tracker.add_expense(10000)
    tracker.add_expense(5000)

    statistics = tracker.get_statistics()

    assert statistics["income_count"] == 2
    assert statistics["expense_count"] == 2
    assert statistics["total_income"] == 80000
    assert statistics["total_expense"] == 15000
    assert statistics["balance"] == 65000
    assert statistics["average_income"] == 40000
    assert statistics["average_expense"] == 7500
    assert statistics["highest_income"] == 50000
    assert statistics["lowest_income"] == 30000
    assert statistics["highest_expense"] == 10000
    assert statistics["lowest_expense"] == 5000


def test_empty_statistics():
    tracker = FinanceTracker()

    statistics = tracker.get_statistics()

    assert statistics["income_count"] == 0
    assert statistics["expense_count"] == 0
    assert statistics["total_income"] == 0
    assert statistics["total_expense"] == 0
    assert statistics["balance"] == 0
    assert statistics["average_income"] is None
    assert statistics["average_expense"] is None
    assert statistics["highest_income"] is None
    assert statistics["lowest_income"] is None
    assert statistics["highest_expense"] is None
    assert statistics["lowest_expense"] is None


def test_to_dict():
    tracker = FinanceTracker()

    tracker.add_income(50000)
    tracker.add_expense(10000)

    data = tracker.to_dict()

    assert data == {
        "transactions": [
            {
                "amount": 50000,
                "transaction_type": "income",
                "category": "other",
                "description": "",
            },
            {
                "amount": 10000,
                "transaction_type": "expense",
                "category": "other",
                "description": "",
            },
        ]
    }


def test_load_data():
    tracker = FinanceTracker()

    data = {
        "incomes": [50000, 30000],
        "expenses": [10000],
    }

    tracker.load_data(data)

    assert tracker.get_incomes() == [50000, 30000]
    assert tracker.get_expenses() == [10000]
    assert tracker.calculate_balance() == 70000


def test_load_data_with_missing_keys():
    tracker = FinanceTracker()

    tracker.load_data({})

    assert tracker.get_incomes() == []
    assert tracker.get_expenses() == []


def test_add_income_creates_transaction():
    tracker = FinanceTracker()

    tracker.add_income(
        50000,
        category="salary",
        description="August salary",
    )

    transactions = tracker.get_transactions()

    assert len(transactions) == 1
    assert transactions[0].amount == 50000
    assert transactions[0].transaction_type == "income"
    assert transactions[0].category == "salary"
    assert transactions[0].description == "August salary"


def test_add_expense_creates_transaction():
    tracker = FinanceTracker()

    tracker.add_expense(
        1000,
        category="food",
        description="Groceries",
    )

    transaction = tracker.get_transactions()[0]

    assert transaction.amount == 1000
    assert transaction.transaction_type == "expense"
    assert transaction.category == "food"


def test_transactions_keep_order():
    tracker = FinanceTracker()

    tracker.add_income(50000, category="salary")
    tracker.add_expense(1000, category="food")
    tracker.add_income(5000, category="freelance")

    transactions = tracker.get_transactions()

    assert transactions[0].transaction_type == "income"
    assert transactions[0].category == "salary"

    assert transactions[1].transaction_type == "expense"
    assert transactions[1].category == "food"

    assert transactions[2].transaction_type == "income"
    assert transactions[2].category == "freelance"


def test_get_expenses_by_category():
    tracker = FinanceTracker()

    tracker.add_expense(1000, category="food")
    tracker.add_expense(1500, category="food")
    tracker.add_expense(500, category="transport")
    tracker.add_income(50000, category="salary")

    result = tracker.get_expenses_by_category()

    assert result == {
        "food": 2500,
        "transport": 500,
    }


def test_get_incomes_by_category():
    tracker = FinanceTracker()

    tracker.add_income(50000, category="salary")
    tracker.add_income(10000, category="freelance")
    tracker.add_income(5000, category="freelance")
    tracker.add_expense(1000, category="food")

    result = tracker.get_incomes_by_category()

    assert result == {
        "salary": 50000,
        "freelance": 15000,
    }


def test_empty_category_reports():
    tracker = FinanceTracker()

    assert tracker.get_incomes_by_category() == {}
    assert tracker.get_expenses_by_category() == {}

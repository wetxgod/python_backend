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
    transactions = data["transactions"]

    assert len(transactions) == 2

    assert transactions[0]["amount"] == 50000
    assert transactions[0]["transaction_type"] == "income"
    assert transactions[0]["category"] == "other"
    assert transactions[0]["description"] == ""
    assert transactions[0]["created_at"]

    assert transactions[1]["amount"] == 10000
    assert transactions[1]["transaction_type"] == "expense"
    assert transactions[1]["category"] == "other"
    assert transactions[1]["description"] == ""
    assert transactions[1]["created_at"]


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


def test_filter_transactions_by_type():
    tracker = FinanceTracker()

    tracker.add_income(50000, category="salary")
    tracker.add_expense(1000, category="food")
    tracker.add_expense(500, category="transport")

    transactions = tracker.filter_transactions(transaction_type="expense")

    assert len(transactions) == 2
    assert all(
        transaction.transaction_type == "expense" for transaction in transactions
    )


def test_filter_transactions_by_category():
    tracker = FinanceTracker()

    tracker.add_expense(1000, category="food")
    tracker.add_expense(1500, category="food")
    tracker.add_expense(500, category="transport")

    transactions = tracker.filter_transactions(category="food")

    assert len(transactions) == 2
    assert all(transaction.category == "food" for transaction in transactions)


def test_filter_transactions_by_type_and_category():
    tracker = FinanceTracker()

    tracker.add_income(5000, category="freelance")
    tracker.add_expense(1000, category="freelance")
    tracker.add_expense(500, category="food")

    transactions = tracker.filter_transactions(
        transaction_type="expense",
        category="freelance",
    )

    assert len(transactions) == 1
    assert transactions[0].amount == 1000
    assert transactions[0].transaction_type == "expense"
    assert transactions[0].category == "freelance"


def test_filter_transactions_is_case_insensitive():
    tracker = FinanceTracker()

    tracker.add_expense(1000, category="Food")

    transactions = tracker.filter_transactions(category="food")

    assert len(transactions) == 1


def test_delete_transaction():
    tracker = FinanceTracker()

    tracker.add_income(50000, category="salary")
    tracker.add_expense(1000, category="food")
    tracker.add_expense(500, category="transport")

    deleted_transaction = tracker.delete_transaction(1)
    transactions = tracker.get_transactions()

    assert deleted_transaction.amount == 1000
    assert deleted_transaction.transaction_type == "expense"
    assert deleted_transaction.category == "food"

    assert len(transactions) == 2
    assert transactions[0].category == "salary"
    assert transactions[1].category == "transport"
    assert tracker.calculate_balance() == 49500


def test_delete_first_transaction():
    tracker = FinanceTracker()

    tracker.add_income(50000)
    tracker.add_expense(1000)

    tracker.delete_transaction(0)

    transactions = tracker.get_transactions()

    assert len(transactions) == 1
    assert transactions[0].transaction_type == "expense"
    assert tracker.calculate_balance() == -1000


def test_delete_transaction_with_invalid_index():
    tracker = FinanceTracker()

    tracker.add_income(50000)

    with pytest.raises(
        IndexError,
        match="Transaction not found.",
    ):
        tracker.delete_transaction(5)


def test_delete_transaction_with_negative_index():
    tracker = FinanceTracker()

    tracker.add_income(50000)

    with pytest.raises(IndexError):
        tracker.delete_transaction(-1)


def test_update_transaction():
    tracker = FinanceTracker()

    tracker.add_expense(
        1000,
        category="food",
        description="Groceries",
    )

    updated_transaction = tracker.update_transaction(
        0,
        amount=1500,
        category="transport",
        description="Taxi",
    )

    assert updated_transaction.amount == 1500
    assert updated_transaction.category == "transport"
    assert updated_transaction.description == "Taxi"
    assert updated_transaction.transaction_type == "expense"
    assert tracker.get_total_expense() == 1500


def test_update_only_transaction_category():
    tracker = FinanceTracker()

    tracker.add_income(
        50000,
        category="other",
        description="Salary",
    )

    tracker.update_transaction(
        0,
        category="salary",
    )

    transaction = tracker.get_transactions()[0]

    assert transaction.amount == 50000
    assert transaction.category == "salary"
    assert transaction.description == "Salary"


def test_update_transaction_with_invalid_amount():
    tracker = FinanceTracker()

    tracker.add_expense(1000)

    with pytest.raises(
        ValueError,
        match="Amount must be greater than zero.",
    ):
        tracker.update_transaction(
            0,
            amount=0,
        )


def test_update_missing_transaction():
    tracker = FinanceTracker()

    with pytest.raises(
        IndexError,
        match="Transaction not found.",
    ):
        tracker.update_transaction(
            5,
            amount=1000,
        )


def test_sort_transactions_by_amount_ascending():
    tracker = FinanceTracker()

    tracker.add_expense(1500, category="food")
    tracker.add_income(50000, category="salary")
    tracker.add_expense(500, category="transport")

    transactions = tracker.sort_transactions(
        sort_by="amount",
    )

    assert [transaction.amount for transaction in transactions] == [
        500,
        1500,
        50000,
    ]


def test_sort_transactions_by_amount_descending():
    tracker = FinanceTracker()

    tracker.add_expense(1500)
    tracker.add_income(50000)
    tracker.add_expense(500)

    transactions = tracker.sort_transactions(
        sort_by="amount",
        reverse=True,
    )

    assert [transaction.amount for transaction in transactions] == [
        50000,
        1500,
        500,
    ]


def test_sort_transactions_by_date():
    tracker = FinanceTracker()

    tracker.add_income(50000)
    tracker.add_expense(1000)
    tracker.add_expense(500)

    transactions = tracker.get_transactions()

    transactions[0].created_at = "2026-08-01T10:00:00"
    transactions[1].created_at = "2026-08-03T10:00:00"
    transactions[2].created_at = "2026-08-02T10:00:00"

    sorted_transactions = tracker.sort_transactions(
        sort_by="date",
    )

    assert [transaction.created_at for transaction in sorted_transactions] == [
        "2026-08-01T10:00:00",
        "2026-08-02T10:00:00",
        "2026-08-03T10:00:00",
    ]


def test_sort_transactions_with_invalid_option():
    tracker = FinanceTracker()

    with pytest.raises(
        ValueError,
        match="Invalid sort option.",
    ):
        tracker.sort_transactions(sort_by="category")


def test_sort_transactions_does_not_change_original_order():
    tracker = FinanceTracker()

    tracker.add_income(50000)
    tracker.add_expense(1000)
    tracker.add_expense(500)

    tracker.sort_transactions(
        sort_by="amount",
    )

    original_transactions = tracker.get_transactions()

    assert [transaction.amount for transaction in original_transactions] == [
        50000,
        1000,
        500,
    ]

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

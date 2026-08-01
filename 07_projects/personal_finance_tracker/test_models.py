from models import Transaction


def test_create_transaction():
    transaction = Transaction(
        amount=50000,
        transaction_type="income",
        category="salary",
        description="August salary",
    )

    assert transaction.amount == 50000
    assert transaction.transaction_type == "income"
    assert transaction.category == "salary"
    assert transaction.description == "August salary"


def test_transaction_has_empty_description_by_default():
    transaction = Transaction(
        amount=10000,
        transaction_type="expense",
        category="food",
    )

    assert transaction.description == ""


def test_transaction_to_dict():
    transaction = Transaction(
        amount=10000,
        transaction_type="expense",
        category="food",
        description="Groceries",
    )

    assert transaction.to_dict() == {
        "amount": 10000,
        "transaction_type": "expense",
        "category": "food",
        "description": "Groceries",
    }

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

    data = transaction.to_dict()

    assert data["amount"] == 10000
    assert data["transaction_type"] == "expense"
    assert data["category"] == "food"
    assert data["description"] == "Groceries"
    assert data["created_at"] == transaction.created_at


def test_transaction_from_dict():
    data = {
        "amount": 1500,
        "transaction_type": "expense",
        "category": "food",
        "description": "Groceries",
    }

    transaction = Transaction.from_dict(data)

    assert transaction.amount == 1500
    assert transaction.transaction_type == "expense"
    assert transaction.category == "food"
    assert transaction.description == "Groceries"


def test_transaction_has_creation_date():
    transaction = Transaction(
        amount=1000,
        transaction_type="expense",
        category="food",
    )

    assert transaction.created_at
    assert "T" in transaction.created_at


def test_transaction_from_dict_without_date():
    data = {
        "amount": 1000,
        "transaction_type": "expense",
        "category": "food",
        "description": "Groceries",
    }

    transaction = Transaction.from_dict(data)

    assert transaction.created_at

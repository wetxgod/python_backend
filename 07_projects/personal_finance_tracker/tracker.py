from models import Transaction


class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def _validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

    def add_income(self, amount, category="other", description=""):
        self._validate_amount(amount)

        transaction = Transaction(
            amount=amount,
            transaction_type="income",
            category=category,
            description=description,
        )

        self.transactions.append(transaction)

    def add_expense(self, amount, category="other", description=""):
        self._validate_amount(amount)

        transaction = Transaction(
            amount=amount,
            transaction_type="expense",
            category=category,
            description=description,
        )

        self.transactions.append(transaction)

    def get_incomes(self):
        return [
            transaction.amount
            for transaction in self.transactions
            if transaction.transaction_type == "income"
        ]

    def get_expenses(self):
        return [
            transaction.amount
            for transaction in self.transactions
            if transaction.transaction_type == "expense"
        ]

    def get_total_income(self):
        return sum(self.get_incomes())

    def get_total_expense(self):
        return sum(self.get_expenses())

    def calculate_balance(self):
        return self.get_total_income() - self.get_total_expense()

    def get_income_count(self):
        return len(self.get_incomes())

    def get_expense_count(self):
        return len(self.get_expenses())

    def get_statistics(self):
        incomes = self.get_incomes()
        expenses = self.get_expenses()

        statistics = {
            "income_count": self.get_income_count(),
            "expense_count": self.get_expense_count(),
            "total_income": self.get_total_income(),
            "total_expense": self.get_total_expense(),
            "balance": self.calculate_balance(),
            "average_income": None,
            "average_expense": None,
            "highest_income": None,
            "lowest_income": None,
            "highest_expense": None,
            "lowest_expense": None,
        }

        if incomes:
            statistics["average_income"] = (
                self.get_total_income() / self.get_income_count()
            )
            statistics["highest_income"] = max(incomes)
            statistics["lowest_income"] = min(incomes)

        if expenses:
            statistics["average_expense"] = (
                self.get_total_expense() / self.get_expense_count()
            )
            statistics["highest_expense"] = max(expenses)
            statistics["lowest_expense"] = min(expenses)

        return statistics

    def get_transactions(self):
        return self.transactions.copy()

    def to_dict(self):
        return {
            "transactions": [transaction.to_dict() for transaction in self.transactions]
        }

    def load_data(self, data):
        self.transactions.clear()

        if "transactions" in data:
            for transaction_data in data["transactions"]:
                transaction = Transaction.from_dict(transaction_data)
                self.transactions.append(transaction)

            return

        for amount in data.get("incomes", []):
            self.add_income(amount)

        for amount in data.get("expenses", []):
            self.add_expense(amount)

    def clear_data(self):
        self.transactions.clear()

    def get_expenses_by_category(self):
        expenses_by_category = {}

        for transaction in self.transactions:
            if transaction.transaction_type != "expense":
                continue

            category = transaction.category
            amount = transaction.amount

            if category not in expenses_by_category:
                expenses_by_category[category] = 0

            expenses_by_category[category] += amount

        return expenses_by_category

    def get_incomes_by_category(self):
        incomes_by_category = {}

        for transaction in self.transactions:
            if transaction.transaction_type != "income":
                continue

            category = transaction.category
            amount = transaction.amount

            if category not in incomes_by_category:
                incomes_by_category[category] = 0

            incomes_by_category[category] += amount

        return incomes_by_category

    def filter_transactions(
        self,
        transaction_type=None,
        category=None,
    ):
        result = []

        for transaction in self.transactions:
            if (
                transaction_type is not None
                and transaction.transaction_type != transaction_type
            ):
                continue

            if (
                category is not None
                and transaction.category.lower() != category.lower()
            ):
                continue

            result.append(transaction)

        return result

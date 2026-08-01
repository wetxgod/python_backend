class FinanceTracker:
    def __init__(self):
        self.incomes = []
        self.expenses = []

    def _validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

    def add_income(self, amount):
        self._validate_amount(amount)
        self.incomes.append(amount)

    def add_expense(self, amount):
        self._validate_amount(amount)
        self.expenses.append(amount)

    def get_total_income(self):
        return sum(self.incomes)

    def get_total_expense(self):
        return sum(self.expenses)

    def calculate_balance(self):
        return self.get_total_income() - self.get_total_expense()

    def get_income_count(self):
        return len(self.incomes)

    def get_expense_count(self):
        return len(self.expenses)

    def get_statistics(self):
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

        if self.incomes:
            statistics["average_income"] = (
                self.get_total_income() / self.get_income_count()
            )
            statistics["highest_income"] = max(self.incomes)
            statistics["lowest_income"] = min(self.incomes)

        if self.expenses:
            statistics["average_expense"] = (
                self.get_total_expense() / self.get_expense_count()
            )
            statistics["highest_expense"] = max(self.expenses)
            statistics["lowest_expense"] = min(self.expenses)

        return statistics

    def get_incomes(self):
        return self.incomes.copy()

    def get_expenses(self):
        return self.expenses.copy()

    def to_dict(self):
        return {
            "incomes": self.get_incomes(),
            "expenses": self.get_expenses(),
        }

    def load_data(self, data):
        self.incomes = data.get("incomes", [])
        self.expenses = data.get("expenses", [])

    def clear_data(self):
        self.incomes.clear()
        self.expenses.clear()

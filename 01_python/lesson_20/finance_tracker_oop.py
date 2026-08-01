class FinanceTracker:
    def __init__(self):
        self.incomes = []
        self.expenses = []

    def add_income(self, amount):
        self.incomes.append(amount)

    def add_expense(self, amount):
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
        return {
            "income_count": self.get_income_count(),
            "expense_count": self.get_expense_count(),
            "total_income": self.get_total_income(),
            "total_expense": self.get_total_expense(),
            "balance": self.calculate_balance(),
        }

    def show_history(self):
        print("Income:")
        if not self.incomes:
            print("No income yet.")
        else:
            for income in self.incomes:
                print(f"+ {income}")

        print()

        print("Expenses:")
        if not self.expenses:
            print("No expenses yet.")
        else:
            for expense in self.expenses:
                print(f"- {expense}")
            print()

    def clear_data(self):
        self.incomes.clear()
        self.expenses.clear()
        print("All data cleared.")


tracker = FinanceTracker()

tracker.add_income(50000)
tracker.add_income(30000)

tracker.add_expense(10000)

tracker.show_history()

print()

statistics = tracker.get_statistics()

print(statistics)

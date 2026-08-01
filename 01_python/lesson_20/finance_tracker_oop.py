class FinanceTracker:
    def __init__(self):
        self.incomes = []
        self.expenses = []

    def add_income(self, amount):
        self.incomes.append(amount)

    def add_expense(self, amount):
        self.expenses.append(amount)

    def show_balance(self):
        total_income = sum(self.incomes)
        total_expense = sum(self.expenses)
        balance = total_income - total_expense
        print(f"Balance: {balance}")
        print()

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

    def show_statistics(self):
        total_income = sum(self.incomes)
        total_expense = sum(self.expenses)
        balance = total_income - total_expense
        print(f"Total Income: {total_income}")
        print(f"Total Expense: {total_expense}")
        print(f"Balance: {balance}")

    def clear_data(self):
        self.incomes.clear()
        self.expenses.clear()
        print("All data cleared.")


tracker = FinanceTracker()
tracker.add_income(50000)
tracker.add_income(30000)
tracker.add_expense(10000)

tracker.show_balance()
tracker.show_history()
tracker.show_statistics()

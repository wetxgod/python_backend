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


tracker = FinanceTracker()

tracker.add_income(50_000)
tracker.add_income(30_000)
tracker.add_expense(10_000)

print(f"Total income: {tracker.get_total_income()}")
print(f"Total expense: {tracker.get_total_expense()}")
print(f"Balance: {tracker.calculate_balance()}")
print(f"Income count: {tracker.get_income_count()}")
print(f"Expense count: {tracker.get_expense_count()}")

statistics = tracker.get_statistics()
print(statistics)


#     def show_balance(self):
#         return sum(self.incomes) - sum(self.expenses)

#     def show_history(self):
#         print("Income:")
#         if not self.incomes:
#             print("No income yet.")
#         else:
#             for income in self.incomes:
#                 print(f"+ {income}")

#         print()

#         print("Expenses:")
#         if not self.expenses:
#             print("No expenses yet.")
#         else:
#             for expense in self.expenses:
#                 print(f"- {expense}")
#                 print()

#     def show_statistics(self):
#         total_income = sum(self.incomes)
#         total_expense = sum(self.expenses)
#         balance = total_income - total_expense
#         print(f"Total Income: {total_income}")
#         print(f"Total Expense: {total_expense}")
#         print(f"Balance: {balance}")

#     def clear_data(self):
#         self.incomes.clear()
#         self.expenses.clear()
#         print("All data cleared.")


# tracker = FinanceTracker()
# tracker.add_income(50000)
# tracker.add_income(30000)
# tracker.add_expense(10000)

# print(tracker.show_balance())
# tracker.show_history()
# tracker.show_statistics()

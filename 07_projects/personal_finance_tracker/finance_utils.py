def add_income(incomes, amount):
    incomes.append(amount)


def add_expense(expenses, amount):
    expenses.append(amount)


def calculate_balance(incomes, expenses):
    return sum(incomes) - sum(expenses)

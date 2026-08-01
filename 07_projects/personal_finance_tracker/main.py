from tracker import FinanceTracker

tracker = FinanceTracker()


def pause():
    print()
    input("Press Enter to continue...")


def add_income():
    while True:
        try:
            amount = float(input("Enter income amount: "))
            if amount <= 0:
                print(
                    "Income amount must be a positive number. Please enter a valid number."
                )
                continue
            tracker.add_income(amount)
            print(f"Income of {amount:.2f} added.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def add_expense():
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount < 0:
                print("Expense amount cannot be negative. Please enter a valid number.")
                continue
            if amount == 0:
                print("Amount must be greater than zero. Please enter a valid number.")
                continue
            tracker.add_expense(amount)
            print(f"Expense of {amount:.2f} added.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def show_balance():
    total_income = tracker.get_total_income()
    total_expense = tracker.get_total_expense()
    balance = tracker.calculate_balance()
    print(f"Total Income: {total_income:.2f}")
    print()
    print(f"Total Expense: {total_expense:.2f}")
    print()
    print(f"Balance: {balance:.2f}")


def show_history():
    incomes = tracker.get_incomes()
    expenses = tracker.get_expenses()

    print("Income:")

    if not incomes:
        print("No income yet.")
    else:
        for income in incomes:
            print(f"+ {income:.2f}")

    print()
    print("Expenses:")

    if not expenses:
        print("No expenses yet.")
    else:
        for expense in expenses:
            print(f"- {expense:.2f}")


def show_statistics():
    statistics = tracker.get_statistics()

    print("Statistics:")
    print()
    print(f"Income count: {statistics['income_count']}")
    print(f"Expense count: {statistics['expense_count']}")
    print(f"Total income: {statistics['total_income']:.2f}")
    print(f"Total expense: {statistics['total_expense']:.2f}")
    print(f"Balance: {statistics['balance']:.2f}")

    print()

    if statistics["average_income"] is None:
        print("No income data.")
    else:
        print(f"Average income: {statistics['average_income']:.2f}")
        print(f"Highest income: {statistics['highest_income']:.2f}")
        print(f"Lowest income: {statistics['lowest_income']:.2f}")

    print()

    if statistics["average_expense"] is None:
        print("No expense data.")
    else:
        print(f"Average expense: {statistics['average_expense']:.2f}")
        print(f"Highest expense: {statistics['highest_expense']:.2f}")
        print(f"Lowest expense: {statistics['lowest_expense']:.2f}")


def show_menu():
    print("=" * 35)
    print("Personal Finance Tracker")
    print("=" * 35)

    print("1. Add income")
    print("2. Add expense")
    print("3. Show balance")
    print("4. Show history")
    print("5. Exit")
    print("6. About")
    print("7. Settings")
    print("8. Show statistics")


def handle_choice(choice):
    print(f"You selected: {choice}")
    print()

    if choice == "1":
        add_income()
        pause()

    elif choice == "2":
        add_expense()
        pause()

    elif choice == "3":
        show_balance()
        pause()

    elif choice == "4":
        show_history()
        pause()

    elif choice == "5":
        print("Goodbye!")

    elif choice == "6":
        show_about()
        pause()

    elif choice == "7":
        show_settings()
        pause()

    elif choice == "8":
        show_statistics()
        pause()

    else:
        print("Invalid option. Please try again.")
        pause()


def show_about():
    print("Personal Finance Tracker v1.0")


def show_settings():
    print("Settings will be available soon.")


while True:
    show_menu()
    choice = input("Choose option: ")
    handle_choice(choice)

    if choice == "5":
        break

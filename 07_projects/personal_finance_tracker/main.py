incomes = []
expenses = []


def pause():
    print()
    input("Press Enter to continue...")


def add_income():
    while True:
        try:
            amount = float(input("Enter income amount: "))
            if amount < 0:
                print("Income amount cannot be negative. Please enter a valid number.")
                continue
            if amount == 0:
                print("Amount must be greater than zero. Please enter a valid number.")
                continue
            incomes.append(amount)
            print(f"Income of {amount} added.")
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
            expenses.append(amount)
            print(f"Expense of {amount} added.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def show_balance():
    total_income = sum(incomes)
    total_expense = sum(expenses)
    balance = total_income - total_expense
    print(f"Total Income: {total_income}")
    print()
    print(f"Total Expense: {total_expense}")
    print()
    print(f"Balance: {balance}")


def show_history():
    print("Income:")

    if not incomes:
        print("No income yet.")
    else:
        for income in incomes:
            print(f"- {income}")

    print()

    print("Expenses:")
    if not expenses:
        print("No expenses yet.")
    else:
        for expense in expenses:
            print(f"- {expense}")


def show_statistics():

    income_count = len(incomes)
    expense_count = len(expenses)
    if incomes:
        highest_income = max(incomes)
        lowest_income = min(incomes)
        average_income = sum(incomes) / income_count
    if expenses:
        average_expense = sum(expenses) / expense_count

    print("Statistics:")
    print()
    print(f"Income count: {income_count}")
    if incomes:
        print(f"Average income: {average_income}")
    else:
        print("No income data.")
    print()
    print(f"Expense count: {expense_count}")
    if expenses:
        print(f"Average expense: {average_expense}")
    else:
        print("No expense data.")
    print()
    if incomes:
        print(f"Highest income: {highest_income}")
        print(f"Lowest income: {lowest_income}")


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

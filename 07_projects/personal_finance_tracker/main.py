from storage import load_data, save_data
from tracker import FinanceTracker

tracker = FinanceTracker()
tracker.load_data(load_data())


def pause():
    print()
    input("Press Enter to continue...")


def add_income():
    while True:
        try:
            amount = float(input("Enter income amount: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        category = input("Enter income category: ").strip()
        description = input("Enter description: ").strip()

        if not category:
            category = "other"

        try:
            tracker.add_income(
                amount,
                category=category,
                description=description,
            )
        except ValueError as error:
            print(error)
            continue

        save_data(tracker.to_dict())
        print(f"Income of {amount:.2f} added.")
        break


def add_expense():
    while True:
        try:
            amount = float(input("Enter expense amount: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        category = input("Enter expense category: ").strip()
        description = input("Enter description: ").strip()

        if not category:
            category = "other"

        try:
            tracker.add_expense(
                amount,
                category=category,
                description=description,
            )
        except ValueError as error:
            print(error)
            continue

        save_data(tracker.to_dict())
        print(f"Expense of {amount:.2f} added.")
        break


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
    transactions = tracker.get_transactions()

    if not transactions:
        print("No transactions yet.")
        return

    print("Transaction history:")
    print()

    for index, transaction in enumerate(transactions, start=1):
        if transaction.transaction_type == "income":
            sign = "+"
        else:
            sign = "-"

        print(f"{index}. {sign}{transaction.amount:.2f} " f"| {transaction.category}")

        if transaction.description:
            print(f"   {transaction.description}")


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


def clear_data():
    confirmation = input(
        "Are you sure you want to clear all data? This action cannot be undone. (yes/no): "
    )
    if confirmation.lower() == "yes":
        tracker.clear_data()
        save_data(tracker.to_dict())
        print("All data cleared.")
    else:
        print("Clear data operation canceled.")


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
    print("9. Clear all data")
    print("10. Show category report")
    print("11. Show filtered transactions")
    print("12. Delete transaction")
    print("13. Update transaction")


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
        return False

    elif choice == "6":
        show_about()
        pause()

    elif choice == "7":
        show_settings()
        pause()

    elif choice == "8":
        show_statistics()
        pause()

    elif choice == "9":
        clear_data()
        pause()

    elif choice == "10":
        show_category_report()
        pause()

    elif choice == "11":
        show_filtered_transactions()
        pause()

    elif choice == "12":
        delete_transaction()
        pause()

    elif choice == "13":
        update_transaction()
        pause()

    else:
        print("Invalid option. Please try again.")
        pause()

    return True


def show_about():
    print("Personal Finance Tracker v1.0")


def show_settings():
    print("Settings will be available soon.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ")

        should_continue = handle_choice(choice)

        if not should_continue:
            break


def show_category_report():
    incomes = tracker.get_incomes_by_category()
    expenses = tracker.get_expenses_by_category()

    print("Category report:")
    print()
    print("Income categories:")

    if not incomes:
        print("No income data.")
    else:
        for category, total in incomes.items():
            print(f"{category}: {total:.2f}")

    print()
    print("Expense categories:")

    if not expenses:
        print("No expense data.")
    else:
        for category, total in expenses.items():
            print(f"{category}: {total:.2f}")


def show_filtered_transactions():
    transaction_type = (
        input("Enter type (income/expense or leave empty): ").strip().lower()
    )

    category = input("Enter category or leave empty: ").strip()

    if not transaction_type:
        transaction_type = None

    if not category:
        category = None

    if transaction_type not in (None, "income", "expense"):
        print("Invalid transaction type.")
        return

    transactions = tracker.filter_transactions(
        transaction_type=transaction_type,
        category=category,
    )

    if not transactions:
        print("No matching transactions.")
        return

    print()
    print("Filtered transactions:")

    for index, transaction in enumerate(transactions, start=1):
        sign = "+" if transaction.transaction_type == "income" else "-"

        print(f"{index}. {sign}{transaction.amount:.2f} " f"| {transaction.category}")

        if transaction.description:
            print(f"   {transaction.description}")


def delete_transaction():
    transactions = tracker.get_transactions()

    if not transactions:
        print("No transactions to delete.")
        return

    show_history()
    print()

    try:
        transaction_number = int(input("Enter transaction number to delete: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    transaction_index = transaction_number - 1

    try:
        deleted_transaction = tracker.delete_transaction(transaction_index)
    except IndexError as error:
        print(error)
        return

    save_data(tracker.to_dict())

    print(
        f"Deleted: {deleted_transaction.transaction_type} "
        f"{deleted_transaction.amount:.2f} "
        f"| {deleted_transaction.category}"
    )


def update_transaction():
    transactions = tracker.get_transactions()

    if not transactions:
        print("No transactions to update.")
        return

    show_history()
    print()

    try:
        transaction_number = int(input("Enter transaction number to update: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    transaction_index = transaction_number - 1

    try:
        current_transaction = transactions[transaction_index]
    except IndexError:
        print("Transaction not found.")
        return

    amount_input = input(
        f"Enter new amount [{current_transaction.amount:.2f}]: "
    ).strip()

    category_input = input(
        f"Enter new category [{current_transaction.category}]: "
    ).strip()

    description_input = input(
        f"Enter new description [{current_transaction.description}]: "
    ).strip()

    new_amount = None

    if amount_input:
        try:
            new_amount = float(amount_input)
        except ValueError:
            print("Invalid amount.")
            return

    new_category = category_input or None
    new_description = description_input or None

    try:
        updated_transaction = tracker.update_transaction(
            transaction_index,
            amount=new_amount,
            category=new_category,
            description=new_description,
        )
    except (IndexError, ValueError) as error:
        print(error)
        return

    save_data(tracker.to_dict())

    print(
        f"Updated: {updated_transaction.transaction_type} "
        f"{updated_transaction.amount:.2f} "
        f"| {updated_transaction.category}"
    )


if __name__ == "__main__":
    main()

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


def handle_choice(choice):
    print(f"You selected: {choice}")

    if choice == "1":
        print("Opening income menu...")

    elif choice == "2":
        print("Opening expense menu...")

    elif choice == "3":
        print("Balance selected.")

    elif choice == "4":
        print("History selected.")

    elif choice == "5":
        print("Goodbye!")

    elif choice == "6":
        show_about()

    elif choice == "7":
        show_settings()

    else:
        print("Invalid option. Please try again.")


def show_about():
    print("Personal Finance Tracker v1.0")


def show_settings():
    print("Settings will be available soon.")


show_menu()
choice = input("Choose option: ")
handle_choice(choice)

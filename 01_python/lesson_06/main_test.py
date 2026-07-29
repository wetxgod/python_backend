print("=" * 35)
print(" PERSONAL FINANCE TRACKER ")
print("=" * 35)


print("1. Add income")
print("2. Add expense")
print("3. Show balance")
print("4. Show history")
print("5. Exit")
print("6. About")
print("7. Settings")

choice = input("Choose option: ")

print(f"You selected: {choice}")

if choice == "1":
    print("Income selected.")

elif choice == "2":
    print("Expense selected.")

elif choice == "3":
    print("Balance selected.")

elif choice == "4":
    print("History selected.")

elif choice == "5":
    print("Goodbye!")

elif choice == "6":
    print("About:\nPersonal Finance Tracker v1.0")

elif choice == "7":
    print("Settings will be available soon.")

else:
    print("Invalid option. Please try again.")

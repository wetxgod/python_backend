# with open("notes.txt", "w") as file:
#     file.write("Hello, Python!")


# with open("notes.txt", "r") as file:
#     content = file.read()
# print(content)

# name = input("Enter your name: ")
# with open("user.txt", "w") as file:
#     file.write(name)
# with open("user.txt", "r") as file:
#     content = file.read()
# print(content)

incomes = [50000, 30000, 15000]

with open("incomes.txt", "w") as file:
    file.writelines(f"{income}\n" for income in incomes)
with open("incomes.txt", "r") as file:
    for line in file:
        print(line.strip())


expenses = [20000, 10000, 5000]
with open("expenses.txt", "w") as file:
    file.writelines(f"{expense}\n" for expense in expenses)
with open("expenses.txt", "r") as file:
    for line in file:
        print(line.strip())

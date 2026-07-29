# price = float(input("Enter product price: "))
# quantity = int(input("Enter quantity: "))

# total = price * quantity

# print(f"Total: {total}")

hourly_rate = float(input("Enter hourly rate: "))
hours_worked = float(input("Enter hours worked: "))
gross_salary = hourly_rate * hours_worked
tax = gross_salary * 0.13
net_salary = gross_salary - tax
print(f"Gross Salary: {gross_salary}")
print(f"Tax: {tax}")
print(f"Net Salary: {net_salary}")

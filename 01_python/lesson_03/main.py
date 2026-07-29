pin = 1234
entered_pin = int(input("Enter your PIN: "))
age = int(input("Enter your age: "))
if entered_pin == pin and age >= 18:
    print("Access granted.")
else:
    print("Access denied.")

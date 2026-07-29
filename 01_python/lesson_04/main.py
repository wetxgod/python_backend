# cnt = 0
# total = 0
# while cnt <= 100:
#     total += cnt
#     cnt += 1
# print(total)

# password = input("Enter your password: ")
# if password == "python123":
#     print("Access granted.")
# else:
#     print("Access denied.")


secret_number = 7
attempts = 0
guess = int(input("Guess the secret number (between 1 and 10): "))
while guess != secret_number:
    attempts += 1
    if guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess the secret number (between 1 and 10): "))
print(f"You have made {attempts} attempts.")

# books = [
#     {
#         "title": "1984",
#         "author": "George Orwell",
#         "year": 1949,
#     },
#     {
#         "title": "The Hobbit",
#         "author": "J.R.R. Tolkien",
#         "year": 1937,
#     },
#     {
#         "title": "Dune",
#         "author": "Frank Herbert",
#         "year": 1965,
#     },
# ]
# for book in books:
#     print(f"\nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\n")
# print(len(books))
# oldest_year = books[0]["year"]
# for oldest_book in books:
#     oldest_year = min(oldest_year, oldest_book["year"])
# print(f"The oldest book was published in {oldest_year}.")


users = [
    {"id": 1, "name": "Alex", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
    {"id": 3, "name": "Charlie", "age": 35},
    {"id": 4, "name": "Diana", "age": 28},
    {"id": 5, "name": "Eve", "age": 22},
]

for user in users:
    print(f"Name: {user['name']}")
    print(f"Age: {user['age']}")
    print()

quantity = len(users)
average_age = sum(user["age"] for user in users) / quantity
oldest_user = max(users, key=lambda x: x["age"])
youngest_user = min(users, key=lambda x: x["age"])

print(f"Quantity of users: {quantity}")

print(f"Average age of users: {average_age}")

print(f"Oldest user: {oldest_user['name']} ({oldest_user['age']})")

print(f"Youngest user: {youngest_user['name']} ({youngest_user['age']})")

adult_users = [user for user in users if user["age"] >= 18]
print(f"Adult users: {[user['name'] for user in adult_users]}")

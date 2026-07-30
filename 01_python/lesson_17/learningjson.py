# import json

# book = {"title": "1984", "author": "George Orwell", "year": 1949}

# with open("book.json", "w") as file:
#     json.dump(book, file, indent=4)
# print(book["title"])
# print(book["author"])
# print(book["year"])

import json

student = {"name": "Wet", "age": 19, "city": "Moscow", "favorite_language": "Python"}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    user = json.load(file)
print(user)
print(f"Name: {user['name']}")
print(f"Age: {user['age']}")
print(f"City: {user['city']}")
print(f"Favorite language: {user['favorite_language']}")

students = [{"name": "Alex", "age": 20}, {"name": "Ivan", "age": 21}]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)
with open("students.json", "r") as file:
    users = json.load(file)
print()
print(users)
for user in users:
    print(f"Name: {user['name']}, Age: {user['age']}")

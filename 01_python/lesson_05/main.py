# languages = ["Python", "Java", "Go", "C#"]
# languages.append("Rust")
# languages.remove("Java")

# for language in languages:
#     print(language)


# grades = [5, 4, 3, 5, 5]
# total = 0
# for grade in grades:
#     total += grade
# print(total)


grades = [5, 4, 3, 5, 4]
total = 0
highest_grade = max(grades)
lowest_grade = min(grades)
for grade in grades:
    total += grade

print("Grades:")
for grade in grades:
    print(grade)
print()
print("Total:", total)
print()
print("Average:", total / len(grades))
print()
print("Highest Grade:", highest_grade)
print()
print("Lowest Grade:", lowest_grade)

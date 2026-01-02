import random
students = ["Rohit", "Amit", "Ritik", "Abishek", "Rocky", "Razz"]
volunteers = random.sample(students, 3)

print("Selected volunteers for the three students a presentation: ")
for student in volunteers:
    print(student)

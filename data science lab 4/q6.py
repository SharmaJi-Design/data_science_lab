from functools import reduce

students = ["Rohit", "Amit", "Rocky", "Razz"]

scores = [85, 92, 78, 90]

paired = list(zip(students, scores))
print("Student and their scores:")
for student, score in paired:
    print(f"{student}: {score}")

total_score = reduce(lambda x, y: x + y, scores)
print("\nTotal sum of all scores:", total_score)

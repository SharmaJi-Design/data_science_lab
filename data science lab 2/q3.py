# Q.3. Student Marks Manager 
# Store student names as keys and marks (list of integers) as values in a dictionary. Compute 
# each student’s average and grade (A/B/C/D). Print the top 2 students based on average marks.

n = int(input("Enter number of students: "))

students = {}

for _ in range(n):
    name = input("Enter student name: ")
    marks = input("Enter marks separated by space: ")
    marks_list = list(map(int, marks.split()))
    students[name] = marks_list

def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'D'
student_avg_grade = {}
for name, marks in students.items():
    avg = sum(marks) / len(marks)
    grade = get_grade(avg)
    student_avg_grade[name] = (avg, grade)

print("\nStudent Details:")
for name, (avg, grade) in student_avg_grade.items():
    print(f"{name} → Average: {round(avg, 2)}, Grade: {grade}")

top_students = sorted(student_avg_grade.items(), key=lambda x: x[1][0], reverse=True)

print("\nTop 2 Students:")
for student in top_students[:2]:
    name, (avg, grade) = student
    print(f"{name} → Average: {round(avg, 2)}, Grade: {grade}")




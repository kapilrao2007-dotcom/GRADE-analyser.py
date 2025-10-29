# gradebook_analyzer.py
# Author: [Kapil]
# Date: [29/10/2025]
# Title: Simple GradeBook Analyzer

def get_students():
    students = {}
    n = int(input("How many students? "))
    for i in range(n):
        name = input(f"Enter student {i+1} name: ")
        marks = float(input(f"Enter marks for {name}: "))
        students[name] = marks
    return students

def statistics(marks):
    avg = sum(marks) / len(marks)
    med = sorted(marks)[len(marks)//2] if len(marks)%2 != 0 else \
        (sorted(marks)[len(marks)//2-1] + sorted(marks)[len(marks)//2]) / 2
    return avg, med, max(marks), min(marks)

def assign_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

students = get_students()
marks = list(students.values())
avg, med, highest, lowest = statistics(marks)

grades = {name: assign_grade(score) for name, score in students.items()}
passed = [name for name, score in students.items() if score >= 40]
failed = [name for name, score in students.items() if score < 40]

print("Name\t\tMarks\t\tGrade")
print("-" * 38)

for name in students:
    print(f"{name}\t\t{students[name]}\t\t{grades[name]}")
print("-" * 38)
print()
print(f"Average: {avg:.2f}")
print()
print(f"Median: {med:.2f}")
print()
print(f"Highest: {highest}")
print()
print(f"Lowest: {lowest}")
print()
print(f"Passed ({len(passed)}): {', '.join(passed)}" if passed else "Passed: none")
print()
print(f"Failed ({len(failed)}): {', '.join(failed)}" if failed else "Failed: none")

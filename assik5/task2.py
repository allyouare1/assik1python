import json

INPUT_FILE = "students.json"
OUTPUT_FILE = "students_updated.json"

def average(grades):
    if not grades:  
        return 0.0
    return sum(grades) / len(grades)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    grades = student.get("grades", [])
    student["average_grade"] = round(average(grades), 2)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(students, f, indent=2)

print(f"Done. Updated file saved as: {OUTPUT_FILE}")
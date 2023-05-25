students = {
    "tom" : 82,
    "jerry" : 93,
    "joon" : 99,
    "misha" : 80,
    "amy" : 74,
    "jhon" : 64
}

def grading(score: int):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score < 70: return "F"

for key, value in students.items():
    print(f"{key} - {value} - ", grading(value))
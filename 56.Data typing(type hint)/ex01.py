# Data Types
# int, float, str, bool

# casting, dynamic typing
# int(3.5) => Casting

age: int = 0
name: str = "JenSeop"
height: float = 6.0
is_student: bool = True
print(age)
print(name)
print(height)
print(is_student)

# Type Hints
def enter_school(is_student: bool) -> bool:
    if is_student:
        return True
    else:
        return False

# How to check the type ofparameter?
if enter_school(is_student):
    print("Student!")
else:
    print("Isn't Student!")
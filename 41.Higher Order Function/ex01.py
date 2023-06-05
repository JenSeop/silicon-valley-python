# Higher order function
# 1. A function is an instance of the Object type.
# 2. You can store the function in a variable.
# 3. You can pass the function as a parameter to another function.
# 4. You can return the function from a function.
# 5. You can store them in data structures such as hash tables.

def add(num1, num2):
    return (num1 + num2)

def sub(num1, num2):
    return (num1 - num2)

def mul(num1, num2):
    return (num1 * num2)

def div(num1, num2):
    return (num1 / num2)

def calc(num1, num2, func):
    return func(num1, num2)

print("add => ", calc(2, 2, add))
print("sub => ", calc(2, 2, sub))
print("mul => ", calc(2, 2, mul))
print("div => ", calc(2, 2, div))
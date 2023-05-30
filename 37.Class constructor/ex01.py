# Custom class
# naming convention
# PascalCase : class name
# camelCase : object name
# snake_case : anything else

class Car:
  def __init__(self, color, engine_type):
    self.color = color
    self.engine_type = engine_type

tesla = Car("green", "electric")
# tesla.color = "red"
# tesla.engine_type = "electric"

# print(tesla.color)
# print(tesla.engine_type)

# How to list all the attributes?
print(vars(tesla))

# constructor
# def __init__(self):
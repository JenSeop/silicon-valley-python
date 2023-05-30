class Car:
  def __init__(self, color, engine_type):
    self.color = color
    self.engine_type = engine_type
    self.speed = 0
    self.is_start = False
  
  def start_engine(self):
    self.speed = 0
    self.is_start = True
  
  def speed_up(self, speed):
    self.speed += speed
  
  def speed_down(self, speed):
    self.speed -= speed

tesla = Car("green", "electric")
print(vars(tesla))

tesla.start_engine()
print(vars(tesla))

for _ in range(1, 10):
  tesla.speed_up(1)
  print("spd up => ", tesla.speed)
print(vars(tesla))

for _ in range(1, 10):
  tesla.speed_down(1)
  print("spd down => ", tesla.speed)
print(vars(tesla))
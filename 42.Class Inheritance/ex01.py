# Parents Class
class Car:

    # Constructor
    def __init__(self):
        # Attribute
        self.wheel_count = 4
        self.door_count = 2
    
    # Method
    def start(self):
        print(self, "started...")
    
    # Method
    def drive(self):
        print(self, "driving...")

# Child Class
class ElectricCar(Car):

    def __init__(self):
        # Parents Method call by super
        super().__init__()
    
    def start(self):
        super().start()
        print(self, "No sound...")

# Child Class
class CombustionEngineCar(Car):

    def __init__(slef):
        super().__init__()
    
    def start(self):
        super().start()
        print(self, "vrooom...")

ec = ElectricCar()
ec.start()
ec.drive()
print(id(ec))
print("-------")

cec1 = CombustionEngineCar()
cec1.start()
cec1.drive()
print(id(cec1))
print("-------")

cec2 = CombustionEngineCar()
print(id(cec2))
print("-------")

cec3 = CombustionEngineCar()
print(id(cec3))
print("-------")
from car import Car

tesla = Car(color = "green", engine_type = "electric")

tesla.start_engine()

for i in range(1, 5):
    tesla.speed_up(1)
    print(tesla.speed)

for i in range(1, 5):
    tesla.speed_down(1)
    print(tesla.speed)
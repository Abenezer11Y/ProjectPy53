class BMW:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed
    def display(self):
        print(f"The fuel type and max speed of the car is respectively {self.fuel_type} and {self.max_speed}km/h")

class Ferrari:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed
    def display(self):
        print(f"The fuel type and max speed of the car is respectively {self.fuel_type} and {self.max_speed}km/h")

Car_1 = BMW("Petrolium", 450)
Car_2 = BMW("Electric", 500)

Car_1.display()
Car_2.display()
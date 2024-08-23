

class Vehicle:

    vehicle_color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


modelT = Vehicle("Ford", 180, 15)
print("Color: ", modelT.vehicle_color, ", Vehicle name: ", modelT.name, "Max speed: ", modelT.max_speed, "Mileage: ", modelT.mileage)

volvo_bus = Bus("Volvo school", 100, 10)
print("Color: ", volvo_bus.vehicle_color, ", Vehicle name: ", volvo_bus.name, "Max speed: ", volvo_bus.max_speed, "Mileage: ", volvo_bus.mileage)

print(volvo_bus.seating_capacity())





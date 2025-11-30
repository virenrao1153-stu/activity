class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"

class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "340 km/h"

def show_car_details(car):
    print("Fuel Type:", car.fuel_type())
    print("Max Speed:", car.max_speed())
    print("---------------------------")

car1 = BMW()
car2 = Ferrari()

show_car_details(car1)
show_car_details(car2)
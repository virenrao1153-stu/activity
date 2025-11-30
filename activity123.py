class Vehicle:
    def _init_(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        
        return self.seating_capacity * 100

class Bus(Vehicle):

    def fare(self):

        total_fare = super().fare()

        maintenance = 0.10 * total_fare

        final_fare = total_fare + maintenance
        return final_fare

school_bus = Bus(50)

print("Total Bus Fare: INR", school_bus.fare())
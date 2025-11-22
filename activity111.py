import math

class Circle:

    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

initial_radius = 5  

circle1 = Circle(initial_radius)

print("Results for Initial Radius:")
print(f"Radius: {initial_radius}")
print(f"Area: {circle1.area():.2f}")
print(f"Perimeter: {circle1.perimeter():.2f}")
print("--------------------------------------")

user_radius = float(input("Enter a radius value: "))

circle2 = Circle(user_radius)

print("\nResults for User Radius:")
print(f"Radius: {user_radius}")
print(f"Area: {circle2.area():.2f}")
print(f"Perimeter: {circle2.perimeter():.2f}")
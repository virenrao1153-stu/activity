def calculate_circumference(radius):
    """
    This function takes the radius of a circle as input
    and returns its circumference using the formula:
    Circumference = 2 * π * r
    """
    pi = 3.14159
    circumference = 2 * pi * radius
    return circumference

print("Welcome! Let's calculate the circumference of a circle.")
radius = float(input("Enter the radius of the circle: "))

result = calculate_circumference(radius)

print(f"The circumference of the circle with radius {radius} is: {result}")
import math

print("Welcome to the Trigonometric Calculator!")
print("----------------------------------------")

angle_deg = float(input("Enter the angle in degrees: "))

angle_rad = math.radians(angle_deg)

sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)

print(f"\nFor angle {angle_deg}°:")
print(f"Sine (sin): {sin_value:.4f}")
print(f"Cosine (cos): {cos_value:.4f}")
print(f"Tangent (tan): {tan_value:.4f}")

print("\n--- Inverse Trigonometric Demo (Optional) ---")
print(f"arcsin({sin_value:.4f}) = {math.degrees(math.asin(sin_value)):.2f}°")
print(f"arccos({cos_value:.4f}) = {math.degrees(math.acos(cos_value)):.2f}°")
print(f"arctan({tan_value:.4f}) = {math.degrees(math.atan(tan_value)):.2f}°")

print("\nThank you for using the Trigonometric Calculator!")
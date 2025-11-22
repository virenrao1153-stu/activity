num = int(input("Enter a number: "))

odd_numbers = [i for i in range(1, num + 1) if i % 2 != 0]

print("Odd numbers up to", num, "=", odd_numbers)

fruits = ["apple", "banana", "mango", "grapes", "orange"]

updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruits list:", fruits)
print("Updated fruits list:", updated_fruits)
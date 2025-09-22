import math
num = float(input("Enter a number: "))
if num < 0:
    print("Sorry, spuare root of a negative number is not real. ")
else:
    sqrt_num = math.sqrt(num)
    print(f"The square root of {num} is {sqrt_num}")
    
print("Welcome to Harshit's Digit Counter Program!")


number = int(input("Enter any number: "))

count = 0  
if number == 0:
    count = 1
else:
    if number < 0:
        number = -number

    while number > 0:
        number = number // 10
        count += 1

print("The total number of digits is:",count)
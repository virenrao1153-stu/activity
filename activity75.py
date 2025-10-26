print("=== Age Checker Program ===")

try:

    age_input = input("Enter your age: ")

    age = int(age_input)

    if age < 0:
        print("Age cannot be negative!")
    else:
        
        if age % 2 == 0:
            print(f"The age {age} is even.")
        else:
            print(f"The age {age} is odd.")

except ValueError:
    
    print("Value Error! Please enter a valid integer age (no letters or symbols).")

except Exception as e:
    
    print(f"An unexpected error occurred: {e}")

print("=== Program Ended ===")
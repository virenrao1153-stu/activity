# Odd/Even Number Checker
# Story: Rahul wants to check if a number is odd or even using this program.

def main():
    print("Welcome to Odd/Even Checker!")
    
    # Taking input from user
    number = int(input("Enter a number: "))
    
    # Checking condition
    if number % 2 == 0:
        print(f"{number} is Even ✅")
    else:
        print(f"{number} is Odd 🔢")

# Run the program
if __name__ == "__main__":
    main()

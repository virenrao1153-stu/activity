# Activity 3: Customise Your Ride

def customise_ride():
    print("Welcome to Ride Customiser!")
    print("Please select your preferred ride category:")
    print("1. Bike")
    print("2. Car")

    category = input("Enter your choice (1 or 2): ")

    if category == '1':
        print("\nYou selected Bike.")
        print("Available Bike types:")
        print("1. Sports Bike")
        print("2. Cruiser Bike")
        bike_choice = input("Enter your choice (1 or 2): ")

        if bike_choice == '1':
            print("\nYou selected a Sports Bike! Great for speed lovers!")
        elif bike_choice == '2':
            print("\nYou selected a Cruiser Bike! Perfect for long comfortable rides.")
        else:
            print("\nInvalid choice. Please restart and select 1 or 2.")

    elif category == '2':
        print("\nYou selected Car.")
        print("Available Car types:")
        print("1. Sedan")
        print("2. SUV")
        car_choice = input("Enter your choice (1 or 2): ")

        if car_choice == '1':
            print("\nYou selected a Sedan! Smooth and elegant ride.")
        elif car_choice == '2':
            print("\nYou selected an SUV! Powerful and spacious.")
        else:
            print("\nInvalid choice. Please restart and select 1 or 2.")
    else:
        print("\nInvalid choice. Please restart and select 1 or 2.")

# Run the program
customise_ride()
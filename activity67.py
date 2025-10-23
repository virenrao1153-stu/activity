def shutdown_program():
    """
    This function asks the user whether they want to shut down.
    It checks the user's input and displays a message accordingly.
    """
    user_input = input("Do you want to shut down the system? (yes/no): ").strip().lower()

    if user_input == "yes":
        print("Shutting down... Please wait.")
    elif user_input == "no":
        print("Shutdown aborted.")
    else:
        print("Sorry, invalid input. Please enter 'yes' or 'no'.")

print("=== Shutdown Confirmation System ===")
shutdown_program()
print("=== Program Ended ===")
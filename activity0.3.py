temperature = int(input("Enter today's temperature in °C: "))
if temperature >= 25:
    print("It's hot! Rohan can wear light clothes.")
elif 15 <= temperature < 25:
    print("The weather is pleasant. Rohan can wear normal clothes.")
else:
    print("It's cold! Rohan should wear warm clothes.")
    
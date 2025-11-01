from datetime import date , time , datetime

today = date.today()
now = datetime.now()
print("Todays date is", today)
print("\ncurrent Date and time is", now)

print("\nDate components", today.year, today.month, today.day)

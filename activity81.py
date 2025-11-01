import calendar  

print("Welcome to the Calendar Module Project!")
print("---------------------------------------")

print("Here are the names of all the months:\n")

for month in range(1, 13):
    print(calendar.month_name[month])

year = int(input("\nEnter a year to display its calendar: "))
print(f"\nHere is the calendar for {year}:\n")
print(calendar.calendar(year))
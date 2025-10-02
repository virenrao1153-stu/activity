import datetime

# Dictionary of festivals (you can expand it as needed)
festivals = {
    "01-01": "New Year's Day",
    "14-01": "Makar Sankranti / Pongal",
    "26-01": "Republic Day (India)",
    "15-08": "Independence Day (India)",
    "02-10": "Gandhi Jayanti",
    "25-12": "Christmas",
}

def get_day_and_festival(date_str):
    try:
        # Convert string to date
        dob = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
        
        # Check range
        if not (datetime.date(1980, 1, 1) <= dob <= datetime.date(2030, 12, 31)):
            return "Date out of range! Please enter between 01-01-1980 and 31-12-2030."
        
        # Get weekday
        day_of_week = dob.strftime("%A")
        
        # Check festival
        key = dob.strftime("%d-%m")
        festival = festivals.get(key, "No festival")
        
        return f"{dob.strftime('%d-%m-%Y')} was a {day_of_week}. Festival: {festival}"
    except ValueError:
        return "Invalid date format! Please enter in DD-MM-YYYY format."

# Example
while True:
    date_input = input("Enter Date of Birth (DD-MM-YYYY) or 'exit' to quit: ")
    if date_input.lower() == "exit":
        break
    print(get_day_and_festival(date_input))

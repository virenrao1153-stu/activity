import datetime
import calendar

# Dictionary of festivals (you can add more)
festivals = {
    "2025-09-05": "Teachers' Day (India)",
    "2025-09-08": "Onam",
    "2025-09-15": "Ganesh Chaturthi",
    "2025-10-02": "Gandhi Jayanti",
    "2025-10-20": "Diwali",
    "2025-11-01": "Kannada Rajyotsava",
    "2025-11-04": "Bhai Dooj",
    "2025-11-14": "Children's Day",
    "2025-12-25": "Christmas"
}

def get_day_and_festival(date_str):
    try:
        # Convert string to date object
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        
        # Check if date is in range (Sep 1 – Dec 31, 2025)
        if datetime.date(2025, 9, 1) <= date_obj <= datetime.date(2025, 12, 31):
            # Get weekday name
            day_name = calendar.day_name[date_obj.weekday()]
            
            # Check festival
            festival = festivals.get(date_str, None)
            if festival:
                return f"{date_str} is a {day_name}. Festival: {festival}"
            else:
                return f"{date_str} is a {day_name}. No festival."
        else:
            return "Date not in range (2025-09-01 to 2025-12-31)."
    except ValueError:
        return "Invalid date format! Use YYYY-MM-DD."

# Run the program
date_input = input("Enter a date (YYYY-MM-DD): ")
print(get_day_and_festival(date_input))

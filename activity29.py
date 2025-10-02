import datetime

def zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"

# ---- Main Program ----
name = input("Enter your name: ")
dob = input("Enter your birthdate (DD-MM-YYYY): ")
day, month, year = map(int, dob.split("-"))

sign = zodiac_sign(day, month)

print(f"\nHello {name}!")
print(f"Your Zodiac Sign is: {sign}")

# Example horoscope messages
horoscope = {
    "Aries": "Today is a good day for new beginnings.",
    "Taurus": "Be patient, good things are coming.",
    "Gemini": "Communication will bring you success.",
    "Cancer": "Focus on family and loved ones.",
    "Leo": "Your leadership will shine today.",
    "Virgo": "Hard work pays off soon.",
    "Libra": "Balance is the key to happiness.",
    "Scorpio": "Trust your instincts.",
    "Sagittarius": "Adventure awaits you.",
    "Capricorn": "Stay disciplined for success.",
    "Aquarius": "Innovation will bring opportunities.",
    "Pisces": "Let your creativity flow."
}

print("Horoscope:", horoscope.get(sign, "Have a wonderful day!"))

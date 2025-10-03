print("=== Report Card Generator ===")

name = input("Enter your friend's name: ")

maths = int(input("Enter marks in Maths (out of 80): "))
english = int(input("Enter marks in English (out of 80): "))
hindi = int(input("Enter marks in Hindi (out of 80): "))
science = int(input("Enter marks in Science (out of 80): "))
sst = int(input("Enter marks in SST (out of 80): "))
computer = int(input("Enter marks in Computer (out of 80): "))
french = int(input("Enter marks in French (out of 50): "))

total = maths + english + hindi + science + sst + computer + french
percentage = (total / 530) * 100   

def get_grade(p):
    if 91 <= p <= 100:
        return "A1"
    elif 81 <= p <= 90:
        return "A2"
    elif 71 <= p <= 80:
        return "B1"
    elif 61 <= p <= 70:
        return "B2"
    elif 51 <= p <= 60:
        return "C1"
    elif 41 <= p <= 50:
        return "C2"
    elif 33 <= p <= 40:
        return "D"
    else:
        return "E1 (Fail)"

grade = get_grade(percentage)

print("\n===== REPORT CARD =====")
print("Name:", name)
print("Maths:", maths, "/ 80")
print("English:", english, "/ 80")
print("Hindi:", hindi, "/ 80")
print("Science:", science, "/ 80")
print("SST:", sst, "/ 80")
print("Computer:", computer, "/ 80")
print("French:", french, "/ 50")
print("---------------------------")
print("Total Marks:", total, "/ 530")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("===========================")

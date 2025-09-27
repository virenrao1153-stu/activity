friends_marks = {
    "Yuvaan": 92,
    "Aiza": 88,
    "Aarav": 81,
    "Vivek": 76,
    "Idaya": 67
}

def get_rank(marks):
    if marks > 90:
        return "A1"
    elif marks > 85:
        return "A2"
    elif marks > 80:
        return "B1"
    elif marks > 75:
        return "B2"
    elif marks > 70:
        return "C1"
    elif marks > 60:
        return "C2"
    elif marks > 50:
        return "D"
    elif marks > 40:
        return "E1"
    else:
        return "E2"
    
    print("Friend Name | Marks | Rank")
print("-" * 30)
for name, marks in friends_marks.items():
    rank = get_rank(marks)
    print(f"{name:<12} | {marks:<5} | {rank}")
    
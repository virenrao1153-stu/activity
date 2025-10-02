def health_check(height_cm, weight_kg, age):
    # Convert height to meters
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)

    # Indian BMI classification
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 23:
        status = "Healthy (Normal)"
    elif 23 <= bmi < 25:
        status = "Overweight (At Risk)"
    elif 25 <= bmi < 30:
        status = "Obese (Class I)"
    else:
        status = "Obese (Class II / Severe)"

    # Ideal weight range (for healthy BMI 18.5 – 23)
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 23 * (height_m ** 2)

    # Approximate ideal height from weight (reverse BMI)
    ideal_height_min = (weight_kg / 23) ** 0.5 * 100
    ideal_height_max = (weight_kg / 18.5) ** 0.5 * 100

    # Age-based suggestion (very rough)
    if age < 18:
        age_msg = "Growth phase: Your weight and height should be judged with pediatric charts."
    elif 18 <= age <= 65:
        age_msg = "Adult phase: Maintain BMI between 18.5–23."
    else:
        age_msg = "Senior phase: Slightly higher BMI (up to 24) may be acceptable."

    return f"""
📊 Health Report:
-------------------------
Height: {height_cm} cm
Weight: {weight_kg} kg
Age   : {age} years

➡️ BMI = {bmi:.2f}
➡️ Status: {status}

✅ Ideal weight for your height: {min_weight:.1f} kg – {max_weight:.1f} kg
✅ For your weight, your height should be between: {ideal_height_min:.1f} cm – {ideal_height_max:.1f} cm
✅ Age-based advice: {age_msg}
"""

# Example loop
while True:
    try:
        print("\n--- Health Checker (Indian BMI) ---")
        h = float(input("Enter your height (cm): "))
        w = float(input("Enter your weight (kg): "))
        a = int(input("Enter your age (years): "))

        print(health_check(h, w, a))

        cont = input("Do you want to check again? (yes/no): ")
        if cont.lower() != "yes":
            break
    except ValueError:
        print("Invalid input! Please enter numbers only.")

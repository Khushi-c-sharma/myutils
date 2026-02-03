def calculate_bmi(weight_kg: float, height_m: float) -> tuple[float, str]:
    """
    Body mass index (BMI) is a screening tool used to estimate body fat based
    on weight and height.

    :param weight_kg: Weight in kilograms
    :param height_m: Height in meters
    :return: (BMI value, BMI category)
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive numbers")

    bmi = weight_kg / (height_m**2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25.0:
        category = "Normal weight"
    elif bmi < 30.0:
        category = "Overweight"
    elif bmi < 35.0:
        category = "Class 1 - Obese"
    elif bmi < 40.0:
        category = "Class 2 - Obese"
    else:
        category = "Class 3 - Obese"

    return round(bmi, 1), category


if __name__ == "__main__":
    bmi, category = calculate_bmi(70, 1.75)
    print(bmi)
    print(category)

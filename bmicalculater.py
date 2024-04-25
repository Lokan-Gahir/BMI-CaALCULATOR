def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight (in kilograms) and height (in meters).
    Formula: BMI = weight / (height ** 2)
    """
    bmi = weight / (height ** 2)
    return bmi

def categorize_bmi(bmi):
    """
    Categorize BMI into health categories based on predefined ranges.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Input weight and height from the user
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Categorize BMI
    category = categorize_bmi(bmi)

    # Display result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()

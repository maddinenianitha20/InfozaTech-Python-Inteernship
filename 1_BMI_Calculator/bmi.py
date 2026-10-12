def calculate_bmi(weight,height):
    bmi=weight/(height**2)
    return bmi
print("========BMI CALCULATOR========")
try:
    weight=float(input("Enter your weight in kg: "))
    height=float(input("Enter your height in meters: "))
    if weight <= 0 or height <= 0:
        print("weight and height must be greater than zero.")
    else:
        bmi=calculate_bmi(weight,height)
        print(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            print("Category : Underweight")
        elif bmi<25:
            print("Category : Normal Weight")
        elif bmi<30:
            print("Category : overweight")
        else:
            print("Category : Obesity")
except ValueError:
    print("Please enter the valid numbers.")


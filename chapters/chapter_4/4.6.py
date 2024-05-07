# Prompt user to enter weight in pounds
weight_in_pounds = eval(input("Enter weight in pounds: "))
KILOGRAMS_PER_POUND = 0.45359237
weight_in_kilograms = weight_in_pounds * KILOGRAMS_PER_POUND

# Prompt user to enter height in feet
height_in_feet = eval(input("Enter feet: "))

# Prompt user to enter height in inches
height_in_inches = eval(input("Enter inches: "))
METERS_PER_INCHES = 0.0254
height_in_meters = ((height_in_feet * 12) + height_in_inches) * METERS_PER_INCHES

# Compute BMI
bmi = weight_in_kilograms / (height_in_meters * height_in_meters)
bmi = round(bmi, 4)

print("BMI is", bmi)

if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You are Normal")
elif bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")

# Prompt user to enter weight in pounds
weight_in_pounds = eval(input("Enter weight in pounds: "))
KILOGRAMS_PER_POUND = 0.45359237
weight_in_kilograms = weight_in_pounds * KILOGRAMS_PER_POUND

# Prompt user to enter height in inches
height_in_inches = eval(input("Enter height in inches: "))
METERS_PER_INCHES = 0.0254
height_in_meters = height_in_inches * METERS_PER_INCHES

# Compute BMI
bmi = weight_in_kilograms / (height_in_meters * height_in_meters)
bmi = int(bmi * 10000) / 10000

print("BMI is", bmi)

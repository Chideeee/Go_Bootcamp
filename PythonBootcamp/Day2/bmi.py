# This program accepts user's weight and height, then outputs the BMI.

body_weight = int(input("Enter your body weight \n"))
height = int(input("Enter your height \n"))
print()
print(body_weight)
print(height)
print()
BMI = body_weight/(height**2)

print("Your BMI is ",  BMI)

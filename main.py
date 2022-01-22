# Prints welcome message
print("Welcome to the Body Mass Index (BMI) calculator")

#calculates user weight
print("Enter weight (in lbs)")
weightInPounds = float(input("  "))

#calculates user height in feet
print("Enter height (in feet)")
feet = float(input("  "))

#calculates user height in inches
print("Enter height (in inches)")
inches = float(input("  "))

#calculates total height
heightInInches = (12 * feet) + inches

# calculates BMI
BMI = (weightInPounds * 703) / (heightInInches * heightInInches)

# prints BMI to user
print("Your BMI is: %.2f" % BMI)
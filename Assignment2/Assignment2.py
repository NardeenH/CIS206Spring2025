#Create a program that asks users for their weight in pounds and their height in feet and inches. Calculate and display their BMI. Format the output to one decimal place. Include a legend that displays value ranges for underweight, normal, and overweight. Be sure to indicate the source for your BMI range recommendations.

from colorama import Fore, Style, init
init()

weight_pounds = float(input("Enter your Weight in pounds: "))
height_feet = int(input("Enter your Height in feet: "))
height_inches = int(input("E nter your Height in inches: "))

total_height_inches = height_feet * 12 + height_inches
height_meters = total_height_inches * 0.0254
weight_kg = weight_pounds * 0.453592

bmi = weight_kg / (height_meters ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

print("\nResults:")
print( "=" * 9)  
print(Fore.GREEN +f"Your BMI is: {bmi:.1f}")
print(Fore.RED + f"Your categorized is: {category}")

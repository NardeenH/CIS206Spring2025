
# Create a program that asks users for their weight in pounds and their height in feet and inches. Calculate and display their BMI. Format the output to one decimal place. Include a legend that displays value ranges for underweight, normal, and overweight. Be sure to indicate the source for your BMI range recommendations.
# This program expands upon a previous assignment by enhancing functionality. 
# I have added data type validation for numeric inputs, range and constraint validation, 


from colorama import Fore, Style, init
init()

def calculate_bmi():
    while True:
        try:
            weight_pounds = float(input("Enter your Weight in pounds (10 - 1000): ")) # Data type validation for the numeric inputs *_^.
            if 10 <= weight_pounds <= 1000: # Range and Constraint Validation:
                break
            else:
                print(Fore.YELLOW + "Error: Weight must be between 10 and 1000 pounds.")
        except ValueError:
            print(Fore.YELLOW + "Error: Invalid input. Please enter a numeric value.")

    while True:
        try:
            height_feet = int(input("Enter your Height in feet (1 - 9): "))
            if 1 <= height_feet <= 9:
                break
            else:
                print(Fore.YELLOW + "Error: Height in feet must be between 1 and 9.")
        except ValueError:
            print(Fore.YELLOW + "Error: Invalid input. Please enter an integer value.")

    while True:
        try:
            height_inches = int(input("Enter your Height in inches (0 - 11): "))
            if 0 <= height_inches <= 11:
                break
            else:
                print(Fore.YELLOW + "Error: Height in inches must be between 0 and 11.")
        except ValueError:
            print(Fore.YELLOW + "Error: Invalid input. Please enter an integer value.")

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

    print(Fore.YELLOW + "\nResults:")
    print(Fore.BLACK + "=" * 20)
    print(Fore.GREEN + f"Your BMI is: {bmi:.1f}")
    print(Fore.BLUE + f"Your category is: {category}")
    print(Fore.BLACK + "=" * 20)

while True:
    calculate_bmi()
    again = input(Fore.CYAN + "Would you like to calculate another BMI? (yes/no): ").strip().lower()
    if again != 'yes':
        print(Fore.MAGENTA + "Thank you for using the BMI Calculator. Goodbye!")
        break

        


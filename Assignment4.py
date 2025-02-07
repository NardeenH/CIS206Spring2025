from colorama import Fore, Style, init

init()

def get_weight(weight_pounds):
    return weight_pounds * 0.453592

def get_inches(height_inches):
    return height_inches * 0.0254

def calculate_bmi_value(weight_pounds, height_inches):
    weight_kg = get_weight(weight_pounds)
    height_meters = get_inches(height_inches)
    return weight_kg / (height_meters ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def calculate_bmi():
    while True:
        try:
            weight_pounds = float(input("Enter your Weight in pounds (10 - 1000): "))
            if 10 <= weight_pounds <= 1000:
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
    bmi = calculate_bmi_value(weight_pounds, total_height_inches)
    category = get_bmi_category(bmi)

    print(Fore.YELLOW + "\nResults:")
    print(Fore.BLACK + "=" * 20)
    print(Fore.GREEN + f"Your BMI is: {bmi:.1f}")
    print(Fore.BLUE + f"Your category is: {category}")
    print(Fore.BLACK + "=" * 20)

def display_bmi_table():
    print( "\nBMI Table (Height: 58-76 inches, Weight: 100-250 pounds)\n" )
    print(Fore.YELLOW + f"{'Weight (lbs)':<15}", end="")
    for height in range(58, 77, 2):
        print(f" {height} in".center(10), end="")
    print("\n" + "_" * 115 )
    for weight in range(100, 251, 10):
        print(Fore.CYAN + f"{weight:<15} |", end="")  
        for height in range(58, 77, 2):
            bmi = calculate_bmi_value(weight, height)  
            print(f"{bmi:.1f}".center(10), end="")
        print(Fore.RESET)  

try:
    while True:
        calculate_bmi()
        again = input(Fore.CYAN + "Would you like to calculate another BMI? (yes/no): ").strip().lower()
        if again != 'yes':
            print(Fore.MAGENTA + "Thank you for using the BMI Calculator. Goodbye!")
            break

    display_bmi_table()

except KeyboardInterrupt:
    print(Fore.RED + "\nProcess interrupted. Goodbye!" + Style.RESET_ALL)

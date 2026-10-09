def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be a positive number. Please try again.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter numeric values only.")

def calculate_bmi():
    print("Welcome to the BMI Calculator!")
    print("-" * 30)
    
    # Getting user input
    weight = get_valid_input("Enter your weight in kilograms (kg): ")
    height = get_valid_input("Enter your height in meters (m): ")
    
    # BMI Calculation: weight / (height^2)
    bmi = weight / (height ** 2)
    
    # Determining category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"
        
    # Displaying results
    print("-" * 30)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Health Category: {category}")

if __name__ == "__main__":
    calculate_bmi()

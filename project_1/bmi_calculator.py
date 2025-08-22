                        # " BMI_Calculator"
# BMI Calculator Program

# User ko welcome message dikhate hain
print("Welcome to BMI Calculator")

# User se weight input lete hain (kilograms mein)
weight = float(input("Apna Weight (kg) daalein: "))

# User se height input lete hain (meters mein)
height = float(input("Apni Height (meter) daalein: "))

# BMI ka calculation karte hain: weight divided by height ka square
bmi = weight / (height ** 2)

# BMI ki value ke basis par category tay karte hain
if bmi < 18.5:
    print("Aapka BMI {:.2f} hai - Category: Underweight")
elif bmi < 24.9:
    print("Aapka BMI {:.2f} hai - Category: Normal weight")
elif bmi < 29.9:
    print("Aapka BMI {:.2f} hai - Category: Overweight")
else:
    print("Aapka BMI {:.2f} hai - Category: Obese")
import random       # Random characters generate karne ke liye
import string       # Letters, digits, symbols ke sets ke liye

# 🔹 Step 1: User se password length input lena
length = int(input("Password ka length batao: "))

# 🔹 Step 2: Character sets define karna
letters = string.ascii_letters      # A-Z aur a-z
digits = string.digits              # 0 se 9 tak
symbols = string.punctuation        # Special characters jaise !@#$%^&*

# 🔹 Step 3: User se character type preferences lena
use_letters = input("Letters chahiye? (y/n): ") == 'y'    # Agar 'y' likha to True
use_digits = input("Digits chahiye? (y/n): ") == 'y'
use_symbols = input("Symbols chahiye? (y/n): ") == 'y'

# 🔹 Step 4: Final character pool banana
char_pool = ""     # Empty string se shuru
if use_letters:
    char_pool += letters     # Letters add karo agar user ne 'y' likha
if use_digits:
    char_pool += digits
if use_symbols:
    char_pool += symbols

# 🔹 Step 5: Agar user ne kuch bhi select nahi kiya
if not char_pool:
    print("Kuch to select karo bhai!")   # Error message
    exit()                               # Program yahin band ho jaye

# 🔹 Step 6: Random password generate karna
password = ''.join(random.choice(char_pool) for _ in range(length))
# Har character randomly pick hoga char_pool se, total 'length' times

# 🔹 Step 7: Final password print karna
print("Generated Password:", password)



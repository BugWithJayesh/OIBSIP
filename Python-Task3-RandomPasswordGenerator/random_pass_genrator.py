import random
import string

def generate_password():
    print("Welcome to the Random Password Generator!")
    print("-" * 45)
    
    # 1. Get Password Length
    while True:
        try:
            length = int(input("Enter password length (minimum 8 characters): "))
            if length < 8:
                print("Error: Password length must be at least 8.")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid number.")

    # 2. Get Character Types
    print("\nSelect character types to include (Type 'y' for yes, 'n' for no):")
    use_upper = input("Include Uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include Lowercase letters? (y/n): ").lower() == 'y'
    use_nums = input("Include Numbers? (y/n): ").lower() == 'y'
    use_syms = input("Include Symbols? (y/n): ").lower() == 'y'

    # 3. Build Character Pool
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_nums:
        char_pool += string.digits
    if use_syms:
        char_pool += string.punctuation

    # 4. Generate Password
    if not char_pool:
        print("\nError: You must select at least one character type! Please run again.")
    else:
        password = "".join(random.choice(char_pool) for _ in range(length))
        print("-" * 45)
        print(f"Your Generated Password: {password}")
        print("-" * 45)

if __name__ == "__main__":
    generate_password()

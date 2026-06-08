import random
import string

def generate_password(length):
    # Define possible characters (letters, digits, symbols)
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    print("=== Secure Password Generator ===")
    try:
        length = int(input("Enter desired password length (e.g., 12): "))
        if length < 4:
            print("Please enter a number greater than 4 for security.")
        else:
            password = generate_password(length)
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Error: Please enter a valid number.") 
import random
import string
import sys

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    """Generate a random password based on the criteria."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")
    
    # Core lowercase letters always included
    chars = string.ascii_lowercase
    mandatory = [random.choice(string.ascii_lowercase)]
    
    if use_uppercase:
        chars += string.ascii_uppercase
        mandatory.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        chars += string.digits
        mandatory.append(random.choice(string.digits))
    if use_special:
        # Standard special characters
        special_chars = "!@#$%^&*()-_=+"
        chars += special_chars
        mandatory.append(random.choice(special_chars))
        
    # Fill remaining password length
    remaining_length = length - len(mandatory)
    password = mandatory + [random.choice(chars) for _ in range(remaining_length)]
    
    # Shuffle to avoid predictable pattern
    random.shuffle(password)
    return "".join(password)

def main():
    print("--- CLI Password Generator ---")
    length = 12
    if len(sys.argv) > 1:
        try:
            length = int(sys.argv[1])
        except ValueError:
            print("Invalid length argument. Using default of 12.")
            
    try:
        pw = generate_password(length)
        print(f"Generated Password: {pw}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

# TODO: Add support for custom character set exclusions in a future release


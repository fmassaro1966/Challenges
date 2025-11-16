import string

def check_password_strength(password):
    """Checks the strength of a password based on specific criteria."""
    min_length = 8
    
    # Initialize criteria flags
    length_valid = len(password) >= min_length
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    # Define symbols using the string module
    symbols = string.punctuation 
    has_symbol = any(char in symbols for char in password)

    # Count how many criteria are met
    criteria_met = sum([length_valid, has_uppercase, has_lowercase, has_digit, has_symbol])

    # Determine strength rating
    if criteria_met == 5:
        strength = "Strong"
        feedback = "Excellent password!"
    elif criteria_met >= 3:
        strength = "Medium"
        feedback = "Consider adding missing elements for a stronger password."
    else:
        strength = "Weak"
        feedback = "Password is very weak. Must be at least 8 characters and include diverse characters."
    
    # Suggest improvements if not strong
    if strength != "Strong":
        missing_criteria = []
        if not length_valid: missing_criteria.append("minimum length (8+ chars)")
        if not has_uppercase: missing_criteria.append("at least one uppercase letter")
        if not has_lowercase: missing_criteria.append("at least one lowercase letter")
        if not has_digit: missing_criteria.append("at least one number")
        if not has_symbol: missing_criteria.append("at least one symbol")
        
        feedback += f" Missing: {', '.join(missing_criteria)}"

    return f"Result: {strength} ({feedback})"

# Allow repeated input until a strong password is given (Stretch Idea)
while True:
    user_password = input("Enter a password to check its strength: ")
    result_message = check_password_strength(user_password)
    print(result_message)
    
    # Exit loop if the password is "Strong"
    if "Result: Strong" in result_message:
        break
# Example usage:
# print(check_password_strength("P@ssw0rd"))
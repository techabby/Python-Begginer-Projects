import re


def strength(password):
    if len(password) < 8:
        return "Your Password is too Short"

    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])"
    if not re.match(pattern, password):
        return "Password is not Complex enough."
    if password.lower() == password or password.upper == password:
        return "Password is not Unique"
    return "Password is Strong"


password = input("Enter your Password to check it's strength: ")
print(strength(password))

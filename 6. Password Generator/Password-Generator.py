import random
import string

print("╔══════════════════════════════════════════════════╗")
print("║       Welcome To Abby's Password Generator       ║")
print("║  Generate Secure and Unique Passwords with Ease  ║")
print("╚══════════════════════════════════════════════════╝")


def pass_gen(len, complexity):
    if complexity == "weak":
        chars = string.ascii_lowercase
    elif complexity == "medium":
        chars = string.ascii_letters + string.digits
    elif complexity == "strong":
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Wrong input. Try again!")
    password = "".join(random.choice(chars) for i in range(len))
    return password


def main():
    complexity = input("""Enter the complexity of password (weak,medium or strong): """)
    len = int(input("Enter the length of the password: "))
    password = pass_gen(len, complexity)
    print("\nYour generated password is:", password)


main()
print("\nThanks for using this password generator!")

print("╔══════════════════════════════════════════════════╗")
print("║           Welcome To Abby's Calculator           ║")
print("╚══════════════════════════════════════════════════╝")


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Cannot divide a number by zero"
    else:
        return a / b


def rem(a, b):
    if b == 0:
        return "Cannot divide a number by zero"
    else:
        return a % b


def exp(a, b):
    return a**b


def ShowMenu():
    print("\nMenu:\t")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("6. Exponential")
    print("7. Exit")


def main():
    while True:
        ShowMenu()
        choice = input("\nEnter your choice: ")
        if choice in ("1", "2", "3", "4", "5", "6", "7"):
            a = int(input("\nEnter the first number: "))
            b = int(input("Enter the second number: "))
            if choice == "1":
                print(f"\nThe value of {a} + {b} is: {a + b}")
            elif choice == "2":
                print(f"\nThe value of {a} - {b} is: {a - b}")
            elif choice == "3":
                print(f"\nThe value of {a} * {b} is: {a * b}")
            elif choice == "4":
                print(f"\nThe value of {a} / {b} is: {a / b}")
            elif choice == "5":
                print(f"\nThe value of {a} % {b} is: {a % b}")
            elif choice == "6":
                print(f"\nThe value of {a} ** {b} is: {a ** b}")
            elif choice == "7":
                print("\nThanks for using this calculator!")
                break
        else:
            print("\nInvalid Option! Please try again.")


main()

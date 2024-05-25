import random


def game(Computer, Me):
    if Computer == Me:
        return None

    if Computer == "Rock":
        if Me == "Paper":
            return True
        else:
            return False

    if Computer == "Paper":
        if Me == "Sissor":
            return True
        else:
            return False

    if Computer == "Sissor":
        if Me == "Rock":
            return True
        else:
            return False


print("Computer Turn : Enter Rock(Rock)  Paper(Paper) or Sissor(Sissor)?  ******\n")
rn = random.randint(1, 3)
if rn == 1:
    Computer = "Paper"
elif rn == 2:
    Computer = "Rock"
elif rn == 3:
    Computer = "Sissor"

Me = input("Your Turn : Enter Rock(Rock)  Paper(Paper) or Sissor(Sissor)?\t")
a = game(Computer, Me)

print(f"\n\tComputer Choose {Computer}")
print(f"\tYou Choose {Me}")

if a == None:
    print("\nIt's a Tie!")
elif a == True:
    print("\nYou Won!")
elif a == False:
    print("\nYou Loose!")

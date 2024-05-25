import random

randNum = random.randint(1, 100)
userGuess = None
guesses = 0


while userGuess != randNum:
    userGuess = int(input("Enter your Guess: "))
    guesses += 1

    if userGuess == randNum:
        print("\nYou Guessed it right!\n")

    else:
        if userGuess < randNum:
            print("Higher Number Please!\n")

        else:
            print("Lower Number PLease!\n")

print(f"You Guessed the Number in {guesses} Guesses. ")

with open(
    "/home/abdullah/Documents/Python Projects/Beginner/3. The Guessing Game/Highscore.txt",
    "r",
) as f:
    Highscore = int(f.read())

if guesses < Highscore:
    print("\nYou have just broken the High Score! ")
    with open(
        "/home/abdullah/Documents/Python Projects/Beginner/3. The Guessing Game/Highscore.txt",
        "w",
    ) as f:
        f.write(str(guesses))

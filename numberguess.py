import random

print("Welcome to GUESS THE NUMBER")


guess_count = 10

print("You have 10 Guesses. The number is between 1-100")

while guess_count > 0:
    minmax = list(range(0, 100))
    random_number = random.randint(0, 100)
    guess1 = int(input("What is your first guess?: "))

    if guess1 == random_number:
        print("WOW, YOU GUESSED FIRST TIME?")
    elif guess1 not in minmax:
        print("Please input a number between 1-100.")
    elif guess1 > random_number:
        print("Try something a little lower...")
    elif guess1 < random_number:
        print("Try something a little higher...")
    else:
        print("Please input a number between 1-100.")

    guess2 = int(input("What will your second guess be?: "))
    if guess2 == random_number:
        print("You Nailed it!")
    elif guess2 not in minmax:
        print("Please input a number between 1-100.")
    elif guess2 > random_number:
        print("Try something a little lower...")
    elif guess2 < random_number:
        print("Try something a little higher...")
    else:
        print("Please input a number between 1-100.")





import random

print("Welcome to GUESS THE NUMBER")
guess_count = 10
print("You have 10 Guesses. The number is between 1-100")
random_number = random.randint(0, 100)
while guess_count > 0:
    minmax = list(range(0, 100))

    guess1 = int(input("What is your guess?: "))

    if guess1 == random_number:
        print("YOU GUESSED IT!")
        guess_count = 0
    elif guess1 not in minmax:
        print("Please input a number between 1-100.")
    elif guess1 > random_number:
        print("Try something a little lower...")
        guess_count = guess_count - 1
    elif guess1 < random_number:
        print("Try something a little higher...")
        guess_count = guess_count - 1
    else:
        print("Please input a number between 1-100.")

print("You ran out of guesses!!")


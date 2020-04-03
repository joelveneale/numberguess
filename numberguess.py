import random
from typing import Any, Union

print("Welcome to GUESS THE NUMBER")
guess_count = 10
higher_guesses = []
lower_guesses = []
print("You have 10 Guesses. The number is between 1-100")
random_number = random.randint(0, 100)
while guess_count > 0:
  minmax = list(range(0, 100))


  guess1 = int(input("What is your guess?: "))
  if guess1 == random_number:
    print("YOU GUESSED IT!")
    guess_count = 0
  elif guess_count == 0:
    print("You ran out of guesses!!")
  elif guess1 not in minmax:
    print("Please input a number between 1-100.")

  elif guess1 > random_number:
    print("Try something a little lower...")
    guess_count = guess_count - 1
    higher_guesses.append(guess1)
    if higher_guesses:
        print("Previous Higher Guesses: " + str(higher_guesses))
        higher_guesses.sort()
    if lower_guesses:
        print("Previous Lower Guesses: " + str(lower_guesses))
        lower_guesses.sort()
    if higher_guesses and lower_guesses:
        print("The number must be between " + (str(lower_guesses[-1]) + " and " + str(higher_guesses[0]) + "..."))
  elif guess1 < random_number:
    print('Try something a little higher...')
    guess_count = guess_count - 1
    lower_guesses.append(guess1)
    if lower_guesses:
        print("Previous Lower Guesses: " + str(lower_guesses))
        lower_guesses.sort()
    if higher_guesses:
        print("Previous Higher Guesses: " + str(higher_guesses))
        higher_guesses.sort()
    if higher_guesses and lower_guesses:
        print("The number must be between " + (str(lower_guesses[-1]) + " and " + str(higher_guesses[0]) + "..."))

  else:
    print("Please input a number between 1-100.")

print("Thanks for playing.")


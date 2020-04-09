import random
from typing import Any, Union



previous_guesses = {
    'higher_guesses': [],
    'lower_guesses': []
}
random_number = random.randint(0, 100)
minmax = list(range(0, 100))
victory = False

def create_previous_guesses(guessInput):
    if guessInput > random_number:
        previous_guesses['higher_guesses'].append(guessInput)
        if previous_guesses['higher_guesses']:
          print("Try something a little lower...")

    elif guessInput < random_number:
        previous_guesses['lower_guesses'].append(guessInput)
        if previous_guesses['lower_guesses']:
          print('Try something a little higher...')


    previous_guesses['higher_guesses'].sort()
    previous_guesses['lower_guesses'].sort()

def run_guessing_game():
    guess_count = 10
    while guess_count > 0 and victory == False:
        guessInput = check_if_guess_is_correct(int(input("What is your guess? ")))
        guess_count = guess_count - 1
    if guess_count == 0:
        print("You ran out of guesses!!")
    return

def check_end_result():
    if victory == True:
        print("Congratulations, you guessed the correct number in " + (10 - guess_count) + "guesses\n")
    else:
        print("Unlucky this time. You didn't guess the number within the guess count.\n")
    print("Thanks for playing.")
    return

def check_if_guess_is_correct(guess1):
    create_previous_guesses(guess1)
    if previous_guesses['higher_guesses'] and previous_guesses['lower_guesses']:
        #print("Previous Lower Guesses: " + str(previous_guesses['lower_guesses']))
        print("The number must be between " + (str(previous_guesses['lower_guesses'][-1]) + " and " + str(
            previous_guesses['higher_guesses'][0]) + "..."))
    if guess1 == random_number:
      print("YOU GUESSED IT!")
      victory = True



    elif guess1 not in minmax:
      print("Please input a number between 1-100.")
    return

def main():
    print("Welcome to GUESS THE NUMBER")
    run_guessing_game()
    check_end_result()
    return


main()
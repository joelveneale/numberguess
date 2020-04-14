import random
import sys
from typing import Any, Union

previous_guesses = {
    'higher': [],
    'lower': []
}
minmax = list(range(0, 100))

def main():
    print("Welcome to GUESS THE NUMBER")
    random_number = random.randint(0, 100)
    guess_count = 10
    victory = False
    run_guessing_game(guess_count, victory, random_number)

def run_guessing_game(guess_count, victory, random_number):
    while guess_count > 0 and victory == False:
        victory = check_if_guess_is_correct(
            validate_input("\nWhat is your guess? "), guess_count, victory, random_number)
        if(victory != 'Failed input validation'):
            guess_count = guess_count - 1
        else:
            victory = False
    if guess_count == 0:
        print("You ran out of guesses!!")
    check_end_result({'guess_count': guess_count, 'victory': victory}, random_number)

def validate_input(input_message):
    guess = input(input_message)
    if guess is "":
        print('Oops. You forgot to input a value. Please try again.')
        return False
    if guess.isdigit():
        return int(guess)
    else:
        print("Oops you didn't input a number. Please try again.")
        return False

def check_if_guess_is_correct(guess, guess_count, victory, random_number):
    if guess == False:
        return 'Failed input validation'
    check_to_change_previous_guesses(guess, random_number)
    if guess_count > 0 and previous_guesses['higher'] and previous_guesses['lower']:
        print("The number must be between " +
              (str(previous_guesses['lower'][-1]) + " and " + str(previous_guesses['higher'][0]) + "..."))
    if guess == random_number:
        return True

    elif guess not in minmax:
        print("Please input a number between 1-100.")
    return False
    
def check_to_change_previous_guesses(guess, random_number):
    if guess > random_number:
        change_previous_guesses(guess, 'higher')

    elif guess < random_number:
        change_previous_guesses(guess, 'lower')

    previous_guesses['lower'].sort()
    previous_guesses['higher'].sort()

def change_previous_guesses(guess, direction):
    opposite_direction = 'lower' if direction == 'higher' else 'higher'
    previous_guesses[direction].append(guess)
    if previous_guesses[direction]:
        print("Try something a little " + opposite_direction + "...")
    return

def check_end_result(result, random_number):
    guess_or_guesses = 'guess' if result['guess_count'] == 9 else 'guesses'
    if result['victory'] == True:
        print("\nCongratulations, you guessed the correct number in " +
              str(10 - result['guess_count']) + " " + guess_or_guesses + "\n")
    else:
        print("\nUnlucky this time. You didn't guess the number within the guess count.\n")
        print("The number was: " + str(random_number))
    shall_we_play_again(input('Do you want to play again? y/n...'))

def shall_we_play_again(play_again):
    if play_again == 'y':
        main()
    else:
        print("\nThanks for playing.\n")
        sys.exit()    

main()

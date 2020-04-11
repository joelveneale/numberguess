import random
import sys

class Guess:

    input = ''
    value = 0
    valid = False
    
    def __init__(self, count=10):
        self.count = count

    def reset_value(self):
        self.input = ''
        self.value = 0
        self.valid = False

    def get_new_value(self, input_message="What is your guess?"):
        print(str(self.count))
        self.reset_value()
        while(not self.valid):
            self.input = input(input_message)
            self.validate_input()
        self.value = int(self.input)
        self.count = self.count - 1
    
    def validate_input(self):
        if self.input is "":
            print('Oops. You forgot to input a value. Please try again.')
        elif not self.input.isdigit():
            print("Oops you didn't input a number. Please try again.")
        else:
            self.valid = True

class PreviousGuesses:

    higher = []
    lower = []

    def reset_values(self):
        self.higher = []
        self.lower = []

    def check_to_change_previous_guesses(self, guess, random_number):
        if guess > random_number:
            self.change_previous_guesses(guess, 'higher')

        elif guess < random_number:
            self.change_previous_guesses(guess, 'lower')

        getattr(self, 'lower').sort()
        getattr(self, 'higher').sort()

    def change_previous_guesses(self, guess, direction):
        opposite_direction = 'lower' if direction == 'higher' else 'higher'
        getattr(self, direction).append(guess)
        if getattr(self, direction):
            print("Try something a little " + opposite_direction + "...")

class Game:

    random_number = random.randint(0, 100)
    min_max = list(range(0, 100))
    victory = False
    
    def __init__(self, guess:Guess, previousGuesses: PreviousGuesses):
        self.guess = guess
        self.previousGuesses = previousGuesses

    def run(self):
        print('running game')
        while self.guess.count > 0 and self.victory == False:
            self.take_turn()
        if self.guess.count == 0:
            print("You ran out of guesses!!")
        self.check_end_result()

    def take_turn(self):
        self.guess.getNewValue()
        print('value' + str(self.guess.value))
        print('random' + str(self.random_number))
        self.previousGuesses.check_to_change_previous_guesses(self.guess.value, self.random_number)
        if self.guess.count > 0 and self.previousGuesses.higher and self.previousGuesses.lower:
            print("The number must be between " +
                (str(self.previousGuesses.lower[-1]) + " and " + str(self.previousGuesses.higher[0]) + "..."))
        if self.guess.value == self.random_number:
            self.victory = True
        elif self.guess.value not in self.min_max:
            print("Please input a number between 1-100.")

    def check_end_result(self):
        guess_or_guesses = 'guess' if self.guess.count == 9 else 'guesses'
        if self.victory == True:
            print("\nCongratulations, you guessed the correct number in " +
                str(10 - self.guess.count) + " " + guess_or_guesses + "\n")
        else:
            print("\nUnlucky this time. You didn't guess the number within the guess count.\n")
            print("The number was: " + str(self.random_number))
        self.shall_we_play_again(input('Do you want to play again? y/n...'))

    def shall_we_play_again(self, play_again):
        if play_again == 'y':
            self.random_number = random.randint(0, 100)
            self.min_max = list(range(0, 100))
            self.victory = False
            self.previousGuesses.resetValues()
            self.run()
        else:
            print("\nThanks for playing.\n")
            sys.exit()
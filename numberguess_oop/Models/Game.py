import random
import sys


class Game:

    random_number = random.randint(0, 100)
    min_max = list(range(0, 100))
    victory = False
    
    def __init__(self, guess, previousGuesses, highscores):
        self.guess = guess
        self.previousGuesses = previousGuesses
        self.highscores = highscores

    def run(self):
        self.highscores.print_highscores()
        print(self.guess.count)
        while self.guess.count > 0 and self.victory == False:
            self.take_turn()
        if self.guess.count == 0 and self.victory == False:
            print("You ran out of guesses!!")
        self.check_end_result()

    def take_turn(self):
        self.guess.get_new_value()
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
            self.highscores.add_highscore(10 - self.guess.count)
        else:
            print("\nUnlucky this time. You didn't guess the number within the guess count.\n")
            print("The number was: " + str(self.random_number))
        self.shall_we_play_again(input('Do you want to play again? y/n...'))

    def shall_we_play_again(self, play_again):
        if play_again == 'y':
            self.random_number = random.randint(0, 100)
            self.min_max = list(range(0, 100))
            self.victory = False
            self.guess.reset_value()
            self.previousGuesses.reset_values()
            self.run()
        else:
            print("\nThanks for playing.\n")
            sys.exit()
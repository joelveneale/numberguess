import random
import sys


class Game:
    guesses = 0
    victory = False
    
    def __init__(self, guess, previousGuesses, highscores, difficulty):
        self.guess = guess
        self.difficulty = difficulty
        self.previousGuesses = previousGuesses
        self.highscores = highscores

    def run(self):
        self.highscores.print_highscores()
        self.difficulty.set_difficulty()
        while self.difficulty.count > 0 and self.victory == False:
            self.take_turn()
        if self.difficulty.count == 0 and self.victory == False:
            print("You ran out of guesses!!")
        self.check_end_result()

    def take_turn(self):
        self.guess.get_new_value()
        self.previousGuesses.check_to_change_previous_guesses(self.guess.value, self.difficulty.random_number)
        self.difficulty.count = self.difficulty.count - 1
        self.guesses = self.guesses + 1
        if self.difficulty.count > 0 and self.previousGuesses.higher and self.previousGuesses.lower:
            print("The number must be between " +
                (str(self.previousGuesses.lower[-1]) + " and " + str(self.previousGuesses.higher[0]) + "..."))
        if self.guess.value == self.difficulty.random_number:
            self.victory = True
        elif self.guess.value not in self.difficulty.min_max:
            print("Please input a number between " + str(self.difficulty.min_max[0]) + " and " + str(self.difficulty.min_max[-1]) + ".")

    def check_end_result(self):
        guess_or_guesses = 'guess' if self.guesses == 1 else 'guesses'
        if self.victory == True:
            print("\nCongratulations, you guessed the correct number in " +
                str(self.guesses) + " " + guess_or_guesses + "\n")
            self.highscores.difflevel = self.difficulty.level
            self.highscores.add_highscore(self.guesses)
            self.highscores.print_highscores()
        else:
            print("\nUnlucky this time. You didn't guess the number within the guess count.\n")
            print("The number was: " + str(self.difficulty.random_number))
        self.shall_we_play_again(input('Do you want to play again? y/n...'))

    def shall_we_play_again(self, play_again):
        if play_again == 'y':
            self.difficulty.reset_difficulty()
            self.victory = False
            self.guess.reset_value()
            self.previousGuesses.reset_values()
            self.guesses = 0
            self.run()
        else:
            print("\nThanks for playing.\n")
            sys.exit()
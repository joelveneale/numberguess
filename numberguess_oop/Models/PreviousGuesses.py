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
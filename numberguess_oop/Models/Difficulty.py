import random

class Difficulty:

    input = ''
    value = 0
    valid = False
    difficulty = 1

    def __init__(self, count=10):
        self.count = count

    def reset_difficulty(self):
        self.input = ''
        self.value = 0
        self.valid = False
        self.difficulty = 1


    def set_difficulty(self, input_question="What difficulty would you like to play at? Press 1 for Easy, press 2 for Medium, or press 3 for Hard: " ):
        self.input = ''
        self.value = 0
        self.valid = False
        self.difficulty = 1

        while (not self.valid):
           self.input = input(input_question)
           self.validate_difficulty()

        self.value = int(self.input)
        if self.value == 1:
            self.difficulty = 1
            print("You have selected easy mode. You have 10 attempts to guess a number between 0-100")
        elif self.value == 2:
            self.difficulty = 2
            print("You have selected medium mode. You have 15 attempts to guess a number between 0-1000")
        elif self.value == 3:
            self.difficulty = 3
            print("You have selected hard mode. You have 20 attempts to guess a number between 0-10000")

        return int(self.difficulty)

    def validate_difficulty(self):
        if self.input is "":
            print('Oops. You forgot to input a value. Please try again.'
                  "\nPress 1 for Easy"
                  "\nPress 2 for Medium"
                  "\nPress 3 for Hard"
                  )
        elif not self.input.isdigit():
            print("Oops you didn't input a number. Please try again."
                  "\nPress 1 for Easy"
                  "\nPress 2 for Medium"
                  "\nPress 3 for Hard"
                  )
        else:
            self.valid = True
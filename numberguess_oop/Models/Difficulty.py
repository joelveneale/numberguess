import random

class Difficulty:

    input = ''
    value = 0
    valid = False
    random_number = random.randint(0, 100)
    min_max = list(range(0, 100))
    count = 10
    level = ''

    def reset_difficulty(self):
        self.input = ''
        self.value = 0
        self.valid = False

    def set_difficulty(self, input_question="What difficulty would you like to play at? Press 1 for Easy, press 2 for Medium, or press 3 for Hard" ):
        self.reset_difficulty()

        while (not self.valid):
           self.input = input(input_question)
           self.validate_difficulty()

        self.value = int(self.input)
        if self.value == 1:
            self.random_number = random.randint(0, 100)
            self.min_max = list(range(0, 100))
            self.count = 10
            self.level = 'easy'
            print("You have selected easy mode. You have 10 attempts to guess a number between 0-100")
        elif self.value == 2:
            self.random_number = random.randint(0, 1000)
            self.min_max = list(range(0, 1000))
            self.count = 15
            self.level = 'medium'
            print("You have selected medium mode. You have 15 attempts to guess a number between 0-1000")
        elif self.value == 3:
            self.random_number = random.randint(0, 10000)
            self.min_max = list(range(0, 10000))
            self.count = 20
            self.level = 'hard'
            print("You have selected hard mode. You have 20 attempts to guess a number between 0-10000")

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
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
        self.count = 10

    def get_new_value(self, input_message="What is your guess? "):
        self.input = ''
        self.value = 0
        self.valid = False
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
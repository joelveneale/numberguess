from classDefinitions import Guess, PreviousGuesses, Game

def main():
    guess = Guess()
    previousGuesses = PreviousGuesses()
    game = Game(guess, previousGuesses)
    game.run()
main()
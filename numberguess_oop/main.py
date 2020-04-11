from Models.Game import Game
from Models.Guess import Guess
from Models.PreviousGuesses import PreviousGuesses
from Models.Highscores import Highscores
from lib.tinydb import TinyDB, Query
db = TinyDB('highscores.json')

def main():
    print("\n--- Welcome to Guess the Number ---\n")
    guess = Guess()
    previousGuesses = PreviousGuesses()
    username = input("What is your username? ")
    highscores = Highscores(db, username)
    game = Game(guess, previousGuesses, highscores)
    game.run()
main()
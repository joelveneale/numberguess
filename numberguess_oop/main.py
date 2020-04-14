from Models.Game import Game
from Models.Guess import Guess
from Models.Difficulty import Difficulty
from Models.PreviousGuesses import PreviousGuesses
from Models.Highscores import Highscores
from lib.tinydb import TinyDB, Query
db = TinyDB('highscores.json')

def main():
    print("\n--- Welcome to Guess the Number ---\n")
    difficulty = Difficulty()
    guess = Guess(difficulty)
    previousGuesses = PreviousGuesses()
    username = input("What is your username? ")
    highscores = Highscores(db, username)
    game = Game(guess, previousGuesses, highscores, difficulty)
    game.run()
main()
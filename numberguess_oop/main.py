from numberguess_oop.Models.Game import Game
from numberguess_oop.Models.Guess import Guess
from numberguess_oop.Models.Difficulty import Difficulty
from numberguess_oop.Models.PreviousGuesses import PreviousGuesses
from numberguess_oop.Models.Highscores import Highscores
from numberguess_oop.lib.tinydb import TinyDB
import pandas as pd

db = TinyDB('highscores.json')

def main():
    print("\n--- Welcome to Guess the Number ---\n")
    difficulty = Difficulty()
    guess = Guess(difficulty)
    previousGuesses = PreviousGuesses()
    username = input("What is your username? ")
    level = difficulty.level
    highscores = Highscores(db, username, level)
    game = Game(guess, previousGuesses, highscores, difficulty)
    game.run()
main()
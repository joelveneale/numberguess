class Highscores:

    def __init__(self, db, username):
        self.db = db
        self.username = username

    def add_highscore(self, score: int):
        self.db.insert({
            'username': self.username, 
            'score': score
        })

    def print_highscores(self):
        print('\nCurrent highscores:\n')
        print(self.db.all(), "\n")

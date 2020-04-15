import pandas as pd



class Highscores:

    def __init__(self, db, username, difflevel):
        self.db = db
        self.username = username
        self.difflevel = difflevel

    def add_highscore(self, score: int):
        self.db.insert({
            'username': self.username,
            'score': score,
            'difficulty': self.difflevel,
        })

    def print_highscores(self):
        print('\nCurrent highscores:\n')
        highscore_df = pd.DataFrame.from_dict(self.db)

        easy_df = highscore_df[highscore_df['difficulty'] == 'easy']

        edf_sorted = easy_df.sort_values(by=['score']).drop(columns=['difficulty']).reset_index(drop=True)
        edf_sorted.index = edf_sorted.index + 1

        medium_df = highscore_df[highscore_df['difficulty'] == 'medium']
        mdf_sorted = medium_df.sort_values(by=['score']).drop(columns=['difficulty']).reset_index(drop=True)
        mdf_sorted.index = mdf_sorted.index + 1
        hard_df = highscore_df[highscore_df['difficulty'] == 'hard']
        hdf_sorted = hard_df.sort_values(by=['score']).drop(columns=['difficulty']).reset_index(drop=True)
        hdf_sorted.index = hdf_sorted.index + 1


        print('\nEasy highscores:\n', edf_sorted, "\n", '\nMedium highscores:\n', mdf_sorted, "\n", '\nHard highscores:\n', hdf_sorted, "\n")


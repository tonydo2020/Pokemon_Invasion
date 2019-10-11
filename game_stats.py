import json


# tracks game stats
# creates a json file that will save the past high scores
# will try to read from that file at the start of the game
class GameStats:

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.ships_left = 0
        self.aliens_start = None
        self.next_speedup = None
        self.aliens_left = None
        self.high_score = None
        self.high_scores_all = None
        self.score = None
        self.level = None
        self.reset_stats()
        self.initialize_high_score()
        self.game_active = False

    def reset_stats(self):

        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def initialize_high_score(self):
        # look for the json file and try to read from it
        try:
            with open('pastScores.json', 'r') as file:
                self.high_scores_all = json.load(file)  # Cast to int to verify type
                self.high_scores_all.sort(reverse=True)
                self.high_score = self.high_scores_all[0]
        except (FileNotFoundError, ValueError, EOFError, json.JSONDecodeError, AttributeError, IndexError) as e:
            print(e)
            self.high_scores_all = [0, 0, 0]  # Some issue with the file, going to default
            self.high_score = self.high_scores_all[0]

    def save_high_score(self):
        # save the high scores to the json file
        for i in range(len(self.high_scores_all)):
            if self.score >= self.high_scores_all[i]:
                self.high_scores_all[i] = self.score
                break
        with open('pastScores.json', 'w') as file:
            json.dump(self.high_scores_all, file)

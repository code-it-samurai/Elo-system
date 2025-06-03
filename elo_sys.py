# Elo Ranking system
# Currently supporting 2 player matches
class EloSys:
    def __init__(self, player1_rating, player2_rating, player1_score, player2_score):
        # current rating of each player
        self.player1_rating = player1_rating
        self.player2_rating = player2_rating

        # who won 1 = victory, 0 = defeat, 0.5 = draw
        self.player1_score = player1_score
        self.player2_score = player2_score

        # used to calibrate the sensitivity of the rating system, higher the number -> drastic the changes to elo post match
        self.scaling_factor = 400
        self.k_factor = 32  # recommended default value

    def rating_difference(self, rating1, rating2):
        return rating1 - rating2

    def win_expectancy(self, rating_difference):
        win_expectancy_raw = 1 / (1 + 10 ** ((rating_difference) / self.scaling_factor))
        win_expectancy_in_percentage = (win_expectancy_raw / 1) * 100
        return {win_expectancy_in_percentage, win_expectancy_raw}

    def new_rating(self, old_rating, score, win_expectancy):
        new_rating = old_rating + self.k_factor * (score - win_expectancy)
        return new_rating


elo = EloSys(1600, 100, 0, 1)

# Elo Ranking system
# Currently supporting 2 player matches
class EloSys:
    def __init__(self, player1_rating, player2_rating):
        # current rating of each player
        self.player1_rating = player1_rating
        self.player2_rating = player2_rating

        # expected rating of each player depending on their current rating and scaling factor
        self.player1_win_expectancy = 0
        self.player2_win_expectancy = 0

        # who won 1 = victory, 0 = defeat, 0.5 = draw
        self.player1_score = 0
        self.player2_score = 1

        # used to calibrate the sensitivity of the rating system, higher the number -> drastic the changes to elo post match
        self.scaling_factor = 400
        self.adjustment_factor = 32  # recommended default value

    def calculate_expected(self):
        rating_difference_player1 = self.player2_rating - self.player1_rating
        rating_difference_player2 = self.player1_rating - self.player2_rating

        self.player1_win_expectancy = self.win_expectancy_calculator(
            rating_difference_player1
        )[0]
        self.player2_win_expectancy = self.win_expectancy_calculator(
            rating_difference_player2
        )[0]

        print(self.player1_win_expectancy, self.player1_rating)
        print(self.player2_win_expectancy, self.player2_rating)

    def calculate_updated_ratings(self):
        print("printing updated rating")

    def win_expectancy_calculator(self, rating_difference):
        win_expectancy_raw = 1 / (1 + 10 ** ((rating_difference) / self.scaling_factor))
        win_expectancy_in_percentage = (win_expectancy_raw / 1) * 100
        return [win_expectancy_in_percentage, win_expectancy_raw]


elo = EloSys(1600, 100, 0, 1)
elo.calculate_expected()

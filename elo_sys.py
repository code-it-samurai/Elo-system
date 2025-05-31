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

        # used to calibrate the sensitivity of the rating system, higher the number -> drastic the changes to elo post match
        self.scaling_factor = 400

    def calculate_expected(self):
        rating_difference_player1 = self.player2_rating - self.player1_rating
        self.player1_win_expectancy = 1 / (
            1 + 10 ** ((rating_difference_player1) / 400)
        )
        self.player1_win_expectancy = (self.player1_win_expectancy / 1) * 100

        rating_difference_player2 = self.player1_rating - self.player2_rating
        self.player2_win_expectancy = 1 / (
            1 + 10 ** ((rating_difference_player2) / 400)
        )
        self.player2_win_expectancy = (self.player2_win_expectancy / 1) * 100

    def calculate_updated_ratings(self):
        console.log("calculating change in ratings for both players")


elo = EloSys(1600, 1400)
elo.calculate_expected()

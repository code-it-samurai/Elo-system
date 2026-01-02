import typing


# Elo Ranking system
# Currently supporting 2 player matches
class EloSys:
    def __init__(self, player1_rating, player2_rating, player1_score, player2_score, verbose=False):
        # current rating of each player
        self.player1_rating = player1_rating
        self.player2_rating = player2_rating

        # who won 1 = victory, 0 = defeat, 0.5 = draw
        self.player1_score = player1_score
        self.player2_score = player2_score

        # used to calibrate the sensitivity of the rating system, higher the number -> drastic the changes to elo post match
        self.scaling_factor = 400
        self.k_factor = 32  # recommended default value

        # rating differences
        self.player1_rating_difference = 0
        self.player2_rating_difference = 0

        # win win_expectancies
        self.player1_win_expectancy = 0
        self.player2_win_expectancy = 0

        # control logging output
        self.verbose = verbose

        if self.verbose:
            print("=" * 50)
            print("Elo Rating System - Calculation Started")
            print("=" * 50)
            print(f"Initial Ratings:")
            print(f"  Player 1: {self.player1_rating}")
            print(f"  Player 2: {self.player2_rating}")
            print(f"Match Results:")
            print(f"  Player 1 Score: {self.player1_score} (1=win, 0=loss, 0.5=draw)")
            print(f"  Player 2 Score: {self.player2_score} (1=win, 0=loss, 0.5=draw)")
            print(f"System Parameters:")
            print(f"  K-Factor: {self.k_factor}")
            print(f"  Scaling Factor: {self.scaling_factor}")
            print("=" * 50)

    def rating_difference(self, rating1, rating2):
        return rating2 - rating1

    def win_expectancy(self, rating_difference):
        win_expectancy_raw = round(
            1 / (1 + 10 ** ((rating_difference) / self.scaling_factor)), 2
        )
        win_expectancy_in_percentage = round((win_expectancy_raw / 1) * 100, 2)
        return {
            "win_expectancy_in_percentage": win_expectancy_in_percentage,
            "win_expectancy_raw": win_expectancy_raw,
        }

    def new_rating(self, old_rating, score, win_expectancy):
        new_rating = old_rating + self.k_factor * (score - win_expectancy)
        return new_rating

    def rating_differences(self):
        self.player1_rating_difference = self.player2_rating - self.player1_rating
        self.player2_rating_difference = self.player1_rating - self.player2_rating
        
        if self.verbose:
            print("\n[Step 1] Calculating Rating Differences:")
            print(f"  Player 1 Rating Difference: {self.player2_rating} - {self.player1_rating} = {self.player1_rating_difference}")
            print(f"  Player 2 Rating Difference: {self.player1_rating} - {self.player2_rating} = {self.player2_rating_difference}")
        
        return {
            "player1_rating_difference": self.player1_rating_difference,
            "player2_rating_difference": self.player2_rating_difference,
        }

    def win_expectancies(self):
        # player1
        self.player1_win_expectancy = round(
            1 / (1 + 10 ** ((self.player1_rating_difference) / self.scaling_factor)), 2
        )
        # win_expectancy_in_percentage = (win_expectancy_raw / 1) * 100
        # player2
        self.player2_win_expectancy = round(
            1 / (1 + 10 ** ((self.player2_rating_difference) / self.scaling_factor)), 2
        )
        # win_expectancy_in_percentage = (win_expectancy_raw / 1) * 100
        
        if self.verbose:
            print("\n[Step 2] Calculating Win Expectancies:")
            print(f"  Player 1 Win Expectancy Formula: 1 / (1 + 10^({self.player1_rating_difference}/{self.scaling_factor}))")
            print(f"  Player 1 Win Expectancy: {self.player1_win_expectancy} ({self.player1_win_expectancy * 100}%)")
            print(f"  Player 2 Win Expectancy Formula: 1 / (1 + 10^({self.player2_rating_difference}/{self.scaling_factor}))")
            print(f"  Player 2 Win Expectancy: {self.player2_win_expectancy} ({self.player2_win_expectancy * 100}%)")
        
        return {
            "player1_win_expectancy": self.player1_win_expectancy,
            "player2_win_expectancy": self.player2_win_expectancy,
        }

    def new_ratings(self):
        # player1
        player1_new_rating = self.player1_rating + self.k_factor * (
            self.player1_score - self.player1_win_expectancy
        )
        # player2
        player2_new_rating = self.player2_rating + self.k_factor * (
            self.player2_score - self.player2_win_expectancy
        )
        
        if self.verbose:
            print("\n[Step 3] Calculating New Ratings:")
            print(f"  Player 1 New Rating Formula: {self.player1_rating} + {self.k_factor} * ({self.player1_score} - {self.player1_win_expectancy})")
            player1_change = player1_new_rating - self.player1_rating
            print(f"  Player 1 New Rating: {player1_new_rating:.2f} (change: {player1_change:+.2f})")
            print(f"  Player 2 New Rating Formula: {self.player2_rating} + {self.k_factor} * ({self.player2_score} - {self.player2_win_expectancy})")
            player2_change = player2_new_rating - self.player2_rating
            print(f"  Player 2 New Rating: {player2_new_rating:.2f} (change: {player2_change:+.2f})")
            print("=" * 50)
            print("Calculation Complete!")
            print("=" * 50)
        
        return {
            "player1_new_rating": player1_new_rating,
            "player2_new_rating": player2_new_rating,
        }


# Usage
# elo = EloSys(1600, 1400, 0, 1)
# p1_rating_diff = elo.rating_difference(1600, 1400)
# p2_rating_diff = elo.rating_difference(1400, 1600)
# p1_win_expectancy = elo.win_expectancy(p1_rating_diff)["win_expectancy_raw"]
# p2_win_expectancy = elo.win_expectancy(p2_rating_diff)["win_expectancy_raw"]
# player1_new_rating = elo.new_rating(1600, 0, p1_win_expectancy)
# player2_new_rating = elo.new_rating(1600, 0, p2_win_expectancy)
#
# rating_diffs = elo.rating_differences()
# win_expectancies = elo.win_expectancies()
# new_ratings = elo.new_ratings()
#
# print("For control obsessed users")
# print(
#    p1_rating_diff,
#    p2_rating_diff,
#    p1_win_expectancy,
#    p2_win_expectancy,
#    player1_new_rating,
#    player2_new_rating,
# )
# print("")
# print("standard approach")
# print(rating_diffs, win_expectancies, new_ratings)

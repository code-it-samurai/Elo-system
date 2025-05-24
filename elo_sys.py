class EloSys:
    def __init__(self, player1_rating, player2_rating):
        self.player1_rating = player1_rating
        self.player2_rating = player2_rating
        self.player1_win_expectancy = 0
        self.player2_win_expectancy = 0

    def calculate_expected(self):
        print("player1 rating", self.player1_rating)
        print("player1 rating", self.player1_rating)

        rating_difference_player1 = self.player2_rating - self.player1_rating
        self.player1_win_expectancy = 1 / (
            1 + 10 ** ((rating_difference_player1) / 400)
        )
        self.player1_win_expectancy = (self.player1_win_expectancy / 1) * 100
        print("Player 1's expected rating against Player 2")
        print(round(self.player1_win_expectancy, 2))

        rating_difference_player2 = self.player1_rating - self.player2_rating
        self.player2_win_expectancy = 1 / (
            1 + 10 ** ((rating_difference_player2) / 400)
        )
        self.player2_win_expectancy = (self.player2_win_expectancy / 1) * 100
        print("player 2's expected rating ")
        print(round(self.player2_win_expectancy, 2))


elo = EloSys(1600, 1400)
elo.calculate_expected()

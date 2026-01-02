# Elo Rating System

Implementation of the popular Elo Algorithm
(future plan is to implement this algorithm into ranked tic tac toe game for real ranking system)

A plugin and play rating system for multipler games if you wanna maintain score of each player

Currently supporting only two players but planning to increase it to multiplayers in the future

## Usage

### Basic Usage (without logging)
```python
from elo_sys import EloSys

# Create an Elo system instance
# Player 1 (rating: 1600) loses to Player 2 (rating: 1400)
elo = EloSys(1600, 1400, 0, 1)

# Calculate the new ratings
rating_diffs = elo.rating_differences()
win_expectancies = elo.win_expectancies()
new_ratings = elo.new_ratings()

print(new_ratings)
# Output: {'player1_new_rating': 1575.68, 'player2_new_rating': 1424.32}
```

### With Verbose Logging (to understand calculations)
```python
from elo_sys import EloSys

# Enable verbose logging by setting verbose=True
elo = EloSys(1600, 1400, 0, 1, verbose=True)

# Calculate the new ratings
rating_diffs = elo.rating_differences()
win_expectancies = elo.win_expectancies()
new_ratings = elo.new_ratings()
```

The verbose mode will display detailed step-by-step calculations including:
- Initial ratings and match results
- Rating differences calculation
- Win expectancy formulas and percentages
- New ratings with changes for each player

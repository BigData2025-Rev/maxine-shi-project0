import pandas as pd
from tabulate import tabulate

class ScoreboardManager:
    def __init__(self, filename="scoreboard.json"):
        self.filename = filename
        self.scoreboard = self.loadScoreboard()

    def loadScoreboard(self):
        """
        Load the scoreboard from the JSON file.
        """
        try:
            with open(self.filename, "r") as file:
                return pd.read_json(file)
        except (FileNotFoundError, ValueError):
            # If file doesn't exist or is corrupted, initialize an empty scoreboard
            return pd.DataFrame(columns=["name", "score"])

    def saveScoreboard(self):
        """
        Save the current scoreboard to the JSON file.
        """
        self.scoreboard.to_json(self.filename, orient="records", indent=4)

    def addScore(self, name, score):
        """
        Add or update a player's score.
        """
        if name in self.scoreboard["name"].values:
            # Check the existing score
            existingScore = self.scoreboard.loc[self.scoreboard["name"] == name, "score"].values[0]
            if score > existingScore:
                # Update the score only if the new score is higher
                self.scoreboard.loc[self.scoreboard["name"] == name, "score"] = score
        else:
            # Add a new player
            self.scoreboard = pd.concat(
                [self.scoreboard, pd.DataFrame([{"name": name, "score": score}])],
                ignore_index=True,
            )
        self.saveScoreboard()

    def displayScoreboard(self):
        """
        Print the scoreboard using tabulate.
        """
        if self.scoreboard.empty:
            print("\nNo scores yet. Be the first to play!\n")
        else:
            sortedScoreboard = self.scoreboard.sort_values(by="score", ascending=False)
            print("\n=== Scoreboard ===")
            print(tabulate(sortedScoreboard.head(10), headers="keys", tablefmt="grid", showindex=False))
            print("==================\n")

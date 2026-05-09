import random
from teams import PREMIER_LEAGUE_TEAMS, get_opponents

class FootballManager:
    def __init__(self, player_team):
        self.player_team = player_team
        self.teams = {team: data.copy() for team, data in PREMIER_LEAGUE_TEAMS.items()}
        self.week = 0
        self.season_over = False

    def play_match(self, opponent):
        player_strength = self.teams[self.player_team]["strength"]
        opponent_strength = self.teams[opponent]["strength"]

        player_score = random.randint(0, 3) + (player_strength // 30)
        opponent_score = random.randint(0, 3) + (opponent_strength // 30)

        if player_score > opponent_score:
            result = "WON"
            self.teams[self.player_team]["wins"] += 1
            self.teams[opponent]["losses"] += 1
            self.teams[self.player_team]["points"] += 3
        elif opponent_score > player_score:
            result = "LOST"
            self.teams[self.player_team]["losses"] += 1
            self.teams[opponent]["wins"] += 1
            self.teams[opponent]["points"] += 3
        else:
            result = "DRAW"
            self.teams[self.player_team]["draws"] += 1
            self.teams[opponent]["draws"] += 1
            self.teams[self.player_team]["points"] += 1
            self.teams[opponent]["points"] += 1

        return {
            "opponent": opponent,
            "player_score": player_score,
            "opponent_score": opponent_score,
            "result": result
        }

    def get_standings(self):
        standings = [(team, data["points"], data["wins"], data["losses"], data["draws"])
                    for team, data in self.teams.items()]
        standings.sort(key=lambda x: x[1], reverse=True)
        return standings

    def get_team_stats(self, team):
        return self.teams[team]

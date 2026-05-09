PREMIER_LEAGUE_TEAMS = {
    "Manchester United": {"strength": 85, "wins": 0, "losses": 0, "draws": 0, "points": 0},
    "Manchester City": {"strength": 90, "wins": 0, "losses": 0, "draws": 0, "points": 0},
    "Liverpool": {"strength": 88, "wins": 0, "losses": 0, "draws": 0, "points": 0},
    "Chelsea": {"strength": 82, "wins": 0, "losses": 0, "draws": 0, "points": 0},
    "Arsenal": {"strength": 81, "wins": 0, "losses": 0, "draws": 0, "points": 0},
    "Tottenham": {"strength": 79, "wins": 0, "losses": 0, "draws": 0, "points": 0},
    "Brighton": {"strength": 76, "wins": 0, "losses": 0, "draws": 0, "points": 0},
    "Newcastle": {"strength": 77, "wins": 0, "losses": 0, "draws": 0, "points": 0},
    "Aston Villa": {"strength": 75, "wins": 0, "losses": 0, "draws": 0, "points": 0},
    "West Ham": {"strength": 72, "wins": 0, "losses": 0, "draws": 0, "points": 0},
}

def get_all_teams():
    return list(PREMIER_LEAGUE_TEAMS.keys())

def get_opponents(player_team):
    return [team for team in PREMIER_LEAGUE_TEAMS.keys() if team != player_team]

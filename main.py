#!/usr/bin/env python3

from game import FootballManager
from teams import get_all_teams, get_opponents

def print_welcome():
    print("\n" + "="*50)
    print("  PREMIER LEAGUE FOOTBALL MANAGER")
    print("="*50)
    print("\nWelcome manager! Pick your team and lead them to glory!\n")

def pick_team():
    teams = get_all_teams()
    print("Available teams:")
    for i, team in enumerate(teams, 1):
        print(f"{i}. {team}")

    while True:
        try:
            choice = int(input("\nEnter team number: "))
            if 1 <= choice <= len(teams):
                return teams[choice - 1]
            print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def print_standings(manager):
    print("\n" + "-"*60)
    print("LEAGUE STANDINGS")
    print("-"*60)
    standings = manager.get_standings()
    for i, (team, points, wins, losses, draws) in enumerate(standings, 1):
        marker = " <-- YOU" if team == manager.player_team else ""
        print(f"{i:2}. {team:20} {points:3}pts (W:{wins} D:{draws} L:{losses}){marker}")
    print("-"*60)

def print_menu():
    print("\n" + "="*50)
    print("MAIN MENU")
    print("="*50)
    print("1. Play a match")
    print("2. View standings")
    print("3. View team stats")
    print("4. Quit game")
    print("="*50)

def main():
    print_welcome()
    player_team = pick_team()
    manager = FootballManager(player_team)

    print(f"\nYou are now managing {player_team}!")

    while True:
        print_menu()
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            opponents = get_opponents(player_team)
            print("\nWhich team do you want to play?")
            for i, team in enumerate(opponents, 1):
                print(f"{i}. {team}")

            try:
                opp_choice = int(input("Enter team number: "))
                if 1 <= opp_choice <= len(opponents):
                    opponent = opponents[opp_choice - 1]
                    match_result = manager.play_match(opponent)

                    print(f"\n{'*'*50}")
                    print(f"{player_team} {match_result['player_score']} - {match_result['opponent_score']} {match_result['opponent']}")
                    print(f"Result: {match_result['result']}")
                    print(f"{'*'*50}")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            print_standings(manager)

        elif choice == "3":
            stats = manager.get_team_stats(player_team)
            print(f"\n{player_team} Stats:")
            print(f"  Wins: {stats['wins']}")
            print(f"  Draws: {stats['draws']}")
            print(f"  Losses: {stats['losses']}")
            print(f"  Points: {stats['points']}")
            print(f"  Team Strength: {stats['strength']}")

        elif choice == "4":
            print("\nThanks for playing! Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

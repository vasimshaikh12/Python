import random
import time

teams = ["CSK", "RCB", "RR", "KKR", "GT", "SRH"]
ball_outcomes = [0, 1, 2, 4, 6, "wicket", "no ball", "wide"]

def toss():
    user_call = input("Enter your choice (Head : h / Tail : t): ").lower()
    toss_result = random.choice(["h", "t"])
    print(f"Actual toss: {toss_result}")
    if user_call == toss_result:
        choice = input("You won the toss! What do you want? (bat/bowl): ").lower()
        return choice
    else:
        comp_choice = random.choice(["bat", "bowl"])
        print(f"You lost the toss! Opponent chooses to {comp_choice}")
        return "bowl" if comp_choice == "bat" else "bat"

def simulate_inning(batting_team, bowling_team, target=None):
    print(f"\n----- {batting_team} vs {bowling_team} -----")
    score = 0
    wickets = 0
    ball = 0.0
    over_count = 0
    balls = 0
    while balls < 6 and wickets < 10:
        input("\nEnter key to bowl the ball!! : ")
        outcome = random.choice(ball_outcomes)
        if outcome == "no ball":
            score += 1
            print("It's a NO BALL!")
        elif outcome == "wide":
            score += 1
            print("It's a WIDE BALL!")
        elif outcome == "wicket":
            wickets += 1
            print("WICKET!")
            ball += 0.1
            balls += 1
        else:
            score += outcome
            if outcome == 6:
                print("It's a SIXER!")
            elif outcome == 4:
                print("It's a BOUNDARY!")
            elif outcome == 0:
                print("Dot ball")
            else:
                print(f"It's {outcome} run(s)")
            ball += 0.1
            balls += 1
        
        print(f"Over: ({round(ball,1)})  Score: {score}/{wickets}")

        if target and score > target:
            print(f"\n{batting_team} WON the match!")
            return score
        
    print(f"\n{batting_team} inning ends with {score}/{wickets}")
    return score

def cricket_match():
    print("\nTeams Available: ", "  ".join(teams))
    user_team = input("\nEnter your team: ").upper()
    if user_team not in teams:
        print("Invalid team selected.")
        return
    
    # Opponent selection
    opp_team = random.choice([team for team in teams if team != user_team])
    print(f"Opponent team selected: {opp_team}")
    
    print("\n------------ TOSS TIME ------------")
    user_decision = toss()
    
    if user_decision == "bat":
        team1 = user_team
        team2 = opp_team
    else:
        team1 = opp_team
        team2 = user_team
    
    print(f"\nFirst Inning: {team1} batting")
    target_score = simulate_inning(team1, team2)
    print(f"\n{team2} NEEDS TO DO {target_score+1} runs in 6 balls")

    print(f"\nSecond Inning: {team2} batting")
    second_score = simulate_inning(team2, team1, target=target_score)

    if second_score == target_score:
        print("\nIt's a TIE!")
    elif second_score < target_score:
        print(f"\n{team1} WON the match!")

# Start the match
cricket_match()

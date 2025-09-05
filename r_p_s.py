import random

user_wins = 0
computer_wins = 0

vals = ["rock", "paper", "scissors"]

while True:
    user_input = input("type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input =="q":
        break
    
    if user_input in ["rock", "paper", "scissors"]:
        computer_input = vals[random.randint(0,101)%3]
        if user_input == "rock":
            if computer_input == "rocks":
                print("Both user and computer take rocks no change in score\n")
                continue
            elif computer_input == "paper":
                computer_wins += 1
                print(f"Computer: paper, User: rock --->>>>Computer Wins so--->> Computer Score:- {computer_wins}, User Score: {user_wins}")
            else:
                user_wins += 1
                print(f"Computer: scissors, User: rock --->>>>User Wins so--->>  Computer Score:- {computer_wins}, User Score: {user_wins}")

        elif user_input == "paper":
            if computer_input == "rocks":
                user_wins += 1
                print(f"Computer: rocks, User: paper --->>>> User Wins so--->>  Computer Score:- {computer_wins}, User Score: {user_wins}")

            elif computer_input == "paper":
                print("Both user and computer take paper no change in score\n")
                continue
            else:
                computer_wins += 1
                print(f"Computer: scissors, User: paper --->>>> Computer Wins so--->>  Computer Score:- {computer_wins}, User Score: {user_wins}")

        elif user_input == "scissors":
            if computer_input == "rocks":
                computer_wins += 1
                print(f"Computer: rocks, User: scissors --->>>> Computer Wins so--->>  Computer Score:- {computer_wins}, User Score: {user_wins}")

            elif computer_input == "paper":
                user_wins
                print(f"Computer: paper, User: scissors --->>>> User Wins so--->>  Computer Score:- {computer_wins}, User Score: {user_wins}")

            else:
                print("Both user and computer take paper no change in score\n")
                continue

print(f"User Scores: {user_wins} ||| Computer Scores: {computer_wins}")
quit()
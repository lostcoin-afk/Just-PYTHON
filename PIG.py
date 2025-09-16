import random

def roll():
    return random.randint(1,6)
while True:
    n = input("Enter number of Player (2-4)")

    if n.isdigit():
        n = int(n)
        if n>=2 and n<=4:
            print("Players score list created and initialized")
            break
    else:
        print("Enter a number")
        

max_score = 50
players_score = [0 for _ in range(n)]

while (max(players_score) < max_score):
    for i in range(n):
        print(f"Current Player: {i}'s turn has just started.")
        print(f"Current Player: {i} total score is {players_score[i]}")
        current_score = 0

        while True:
            choice = input(" If you want to continue press (y)")
            if choice.lower() != "y":
                break
            value = roll()
            if value == 1:
                current_score = 0
                print("You rolled a value 1. So your current score is now 0")
                break
            current_score += value
            print(f"you rolled a value {value}")
        players_score[i] += current_score
        print(f"Current Player: {i} total score after turn is {players_score[i]}")

for i in range(len(players_score)):
    print(f"Player {i} score: {players_score[i]} \n")
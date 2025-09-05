import json
print("Welcome to my computer quiz!")

## take user name after asking if they want ot play or not
## Check the user input if yes or no then take user name if no then quit() 

playing = input("Do you want to play?")

if playing != "yes":
    quit()



name = input("Enter your name?")
print (f"{name} is in game.")
score = 0


with open("questions.json","r") as f:
    questions = json.load(f)
print(type(questions))

for q in questions:
    print(f"{q["question"]}")
    print(f"Your choices are:0\n 1. {q["choices"][0]} 2. {q["choices"][1]} 3. {q["choices"][2]} ")
    answer = input("Enter your answer")
    if answer == q["answer"]:
        score += 1
        print("Correct! Your score is:- ",score)
    else:
        score -= 1
        print("Incorrect! Your score is:- ",score)


# PLANNING AHEAD OF THE GAME

# For this game we can increase the json file with questions, rnadomise the order of delivery of questions,
# or even give a custom order such as easy , easy, medium, hard, 
# Then we can implement a front-end for this game using JavaScript such that onClickEvent a a request is sent to the server for verification and the score is sent to the front-end after score calculation.

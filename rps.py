import random

#Define the conditions for wins e.g. Rock > Scissors
CONDITIONS = [["r", "s"], ["p", "r"], ["s", "p"]]

#Generate messages with a style border
def statement_generator(text, symbol):
    length = len(text)+6
    print(symbol*length)
    print(symbol*2 + " "*(len(text)+2) + symbol*2)
    print(symbol*2 + " " + text + " " + symbol*2)
    print(symbol*2 + " "*(len(text)+2) + symbol*2)
    print(symbol*length)

#Turn options into their full name
def get_full_input(text):
    if text == "r":
        return "Rock"
    elif text == "s":
        return "Scissors"
    elif text == "p":
        return "Paper"
    return None

def add_score(score, variable):
    if variable == "Win":
        score[0][1] += 1
    if variable == "Lose":
        score[1][1] += 1
    if variable == "Tie":
        score[2][1] += 1

#Start the game
def start_game():
    #Define variable to track user score
    user_score = [["Wins",0],["Losses",0],["Ties",0]]
    statement_generator("Welcome to Rock, Paper, Scissors", "=")

    #Ask user if they have played before, if no display playing info
    played_before = input("Have you played the game before? [y]/[n]: ")
    #Make sure input is valid
    while played_before != "n" and played_before != "y":
        print("Invalid Input, use [y] or [n]!")
        played_before = input("Have you played the game before? [y]/[n]: ")
    if played_before == "n":
        print("\nYou start by entering your choice. This choice can be rock, paper or scissors.")
        print("\nRock > Scissors")
        print("Paper > Rock")
        print("Scissors > Paper\n")
        print("To quit type 'xxx' instead of entering your choice\n")
    
    #Determine how many rounds to play
    while True:
        playing_rounds = input("How many rounds do you want to play? [infinite] or [a number]: ")
        if playing_rounds == "infinite":
            playing_rounds = 9999999999
            break
        try:
            playing_rounds = int(playing_rounds)
            if playing_rounds < 1:
                print("Invalid Input, use a number higher than 1!")
                continue
            else:
                break
        except:
            continue

    while playing_rounds > 0:
        playing_rounds += -1
        #Get the users choice either Rock, Paper or Scissors
        user_choice = input("What do you choose? [R]ock [P]aper [S]cissors or 'xxx' to quit: ")
        #Make sure users input is valid
        while True:
            if user_choice == "xxx":
                return
            value = get_full_input(user_choice)
            if value == "Rock":
                break
            if value == "Paper":
                break
            if value == "Scissors":
                break
            user_choice = input("What do you choose? [R]ock [P]aper [S]cissors or 'xxx' to quit: ")
            continue

        #Generate random choice for computer
        computer_choice = random.choice(CONDITIONS)
        computer_choice = computer_choice[0]

        #Determine if the user tied, won or lost
        #What runs if user ties
        if computer_choice == user_choice:
            statement_generator("You Tied!! You picked {} and computer picked {}".format(get_full_input(user_choice), get_full_input(computer_choice)), "=")
            add_score(user_score, "Tie")
            statement_generator("Your Score: Wins: {} Losses: {} Ties: {}".format(str(user_score[0][1]),str(user_score[1][1]),str(user_score[2][1])),"=")
            continue

        #Check if the combination exists in win conditions
        try:
            #Run if yes and the user has won
            CONDITIONS.index([user_choice, computer_choice])
            statement_generator("You Win!! You picked {} and computer picked {}".format(get_full_input(user_choice), get_full_input(computer_choice)), "=")
            add_score(user_score, "Win")
        except:
            try:
                #Run if yes and the computer has won
                CONDITIONS.index([computer_choice, user_choice])
                statement_generator("You Lost!! You picked {} and computer picked {}".format(get_full_input(user_choice), get_full_input(computer_choice)), "=")
                add_score(user_score, "Lose")
            except:
        #Run if user has lost
                print("This situation does not exist!")
        statement_generator("Your Score: Wins: {} Losses: {} Ties: {}".format(str(user_score[0][1]),str(user_score[1][1]),str(user_score[2][1])),"=")

#Begin the game
start_game()




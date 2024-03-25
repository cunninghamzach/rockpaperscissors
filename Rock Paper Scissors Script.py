# Rock Paper Scissors Script
# Zach Cunningham - 3.25.2024
# Assignment completed for COMP ENG FUNDAMENTALS - ECET 290 under Dr Harris.

import random # Imported lib for rand int

player = input("Enter player username:\n")
roundnum = 1                                                           # Init counter until round 5 (final round).
pwins = 0                                                              # Init player win counter.
ploss = 0                                                              # Init player loss counter.
ties = 0                                                               # Init tie counter for game.
lossmsg = "You lost round number"                                      # Round loss message.
winmsg = "You won round number"                                        # Round win message.

while roundnum < 6:
    rpsnum = random.randint(0,2)                                       # Value between 0 and 2. Used in below chain.
    userinput = False                                                  # While loop for user input checking.
    print("ROUND",roundnum)
    
    while userinput == False:    
        userrps = input("Please enter one of the following strings:\n rock    paper    scissors\n> ")
        if userrps == "rock": break                                    # If statements checking for valid input.
        elif userrps == "paper": break
        elif userrps == "scissors": break
        else:
            print("You entered an invalid string.\n")
    print("You selected:",userrps)
    
    if rpsnum == 0:                                                    # If/elif chain for computer decision.
        rps = "rock"
    elif rpsnum == 1:
        rps = "paper"
    elif rpsnum == 2:
        rps = "scissors"
    print("The CPU selected:",rps)
    
    if userrps == rps: ties = ties+1 ; break                           # Begin if/elif chain for determining winner
    elif userrps == "rock":
        if rps == "paper":
            ploss = ploss + 1
            print(lossmsg,roundnum)
        elif rps == "scissors":
            pwins = pwins + 1
            print(winmsg,roundnum)
    elif userrps == "paper":
        if rps == "scissors":
            ploss = ploss + 1
            print(lossmsg,roundnum)
        if rps == "rock":
            pwins = pwins + 1
            print(winmsg,roundnum)
    elif userrps == "scissors":
        if rps == "rock":
            ploss = ploss + 1
            print(lossmsg,roundnum)
        elif rps == "paper":
            pwins = pwins + 1
            print(winmsg,roundnum)
    roundnum = roundnum+1
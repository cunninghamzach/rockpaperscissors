# Rock Paper Scissors Script
# Zach Cunningham - 3.25.2024
# Assignment completed for COMP ENG FUNDAMENTALS - ECET 290 under Dr Harris.

import random # Imported lib for rand int

player = input("Enter player username:\n")
roundnum = 1 # Counter until round 5 (final round).

while roundnum < 6:
    rpsnum = random.randint(0,2) # Value between 0 and 2. Used in below chain.
    if rpsnum == 0: # if/elif chain for computer decision.
        rps = "rock"
    elif rpsnum == 1:
        rps = "paper"
    elif rpsnum == 2:
        rps = "scissors"
    roundnum = roundnum+1
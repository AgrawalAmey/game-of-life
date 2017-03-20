# Driver file for Conway's game of life v0

# Import libs
import sys
import json
import numpy as np
from game_of_life import *

# Initialize game module
game = GAME_OF_LIFE()

# Load json file
with open('patterns.json') as pattern_file:
    patterns = json.load(pattern_file)["patterns"]

# just to that the loop starts
contin = 1

while contin:
    # Quick and hacky menu
    print("-------------------------------------------------------------------")
    print("                    Welcome To The Game Of Life                    ")
    print("-------------------------------------------------------------------")
    print("Select one of the following patterns:")

    # Print name of each pattern from file
    for i in range(len(patterns)):
        print(i + 1, ". ", patterns[i]["name"], sep="")

    # Take input
    pattern_num = input('Please enter the pattern number: ')
    pattern_num = int(pattern_num)

    # Load matrix
    x = np.asarray(patterns[pattern_num - 1]["array"])

    print("-------------------------------------------------------------------")

    n = input('Please enter the number of itrations: ')
    n = int(n)

    print("-------------------------------------------------------------------")

    print("Select the render mode:")
    print("1. Render on terminal")
    print("2. Render with matplotlib")
    print("3. Create a video")

    # Take input
    render_mode = input('Please enter the render mode number: ')
    render_mode = int(render_mode)

    # Render
    if(render_mode == 1):
        game.render_terminal(x, n)
    elif(render_mode == 2):
        game.render_matplotlib(x, n)
    elif(render_mode == 3):
        game.save_as_video(x, n)

    print("-------------------------------------------------------------------")
    contin = input('Enter 1 to continue or 0 to exit: ')
    contin = int(contin)

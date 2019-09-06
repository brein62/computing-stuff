import random
import math

def CreatePond():
    pond = [['.' for i in range(15)] for j in range(8)]
    inserted = 0
    while inserted < 3:
        x = math.floor(random.random() * 15) + 1        # generates random x-coordinate from 1 to 15
        y = math.floor(random.random() * 8) + 1         # generates random y-coordinate from 1 to 8
        if (pond[y - 1][x - 1] != 'F'):                 # prevents fish from spawning at same spot
            pond[y - 1][x - 1] = 'F'
            inserted += 1
    return pond

def DisplayPond(pond):
    display = ""
    for row in pond:
        for cell in row:
            display += cell
        display += "\n"
    print(display)

def FeedFish(pond):
    x = input("Enter X coordinate <1 to 15> : ")
    y = input("Enter Y coordinate <1 to 8>  : ")
    if pond[int(y) - 1][int(x) - 1] == 'F':             # there is a fish present
        pond[int(y) - 1][int(x) - 1] = 'H'              # happy fish
    else:
        pond[int(y) - 1][int(x) - 1] = 'P'              # uneaten pellet
    DisplayPond(pond)                                   # display the current state of the pond
    return pond
    

def ThrowStone(pond):
    x = input("Enter X coordinate <1 to 15> : ")
    y = input("Enter Y coordinate <1 to 8>  : ")
    pond[int(y) - 1][int(x) - 1] = 'S'                  # pond array is 0-based, coordinates are 1-based
    DisplayPond(pond)                                   # display the current state of the pond
    return pond

import random

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def play_one_move(col, row, valid_directions, total, move_count):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    options = ["n","e","s","w"]
    victory = False
    direction = random.choice(options)
    direction = direction.lower()
    print("Direction:", direction)
    move_count += 1
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col,row)
        coins = lever(col, row)
        total += coins
        if coins > 0:
            print("You received 1 coin, your total is now {}.".format(total))
    return victory, col, row, total, move_count

def lever(col,row):
    if (col,row) in [(1,2), (2,2), (2,3), (3,2)]:
        #question = input("Pull a lever (y/n): ")
        pull_lever = random.choice(["y", "n"])
        print("Pull a lever (y/n): ", pull_lever)
        if pull_lever == "y":
            return 1
    return 0


# The main program starts here
random.seed(int(input("Input seed: ")))
victory = False
play = True


while play:
    row = 1
    col = 1
    total = 0
    move_count = 0
    while not victory:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row, total, move_count = play_one_move(col, row, valid_directions,total, move_count)
    print("Victory! Total coins {}. Moves {}.".format(total, move_count))
    play_Again = input("Play again (y/n): ")
    if play_Again == "y" or play_Again == "Y":
        play = True
        victory = False
    else:
        play = False
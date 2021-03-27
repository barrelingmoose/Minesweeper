# ##############################################################################
# Developed by: Chandler Kramer
# Date:         3/23/21
# Description:  This is a Minesweeper replica intended to be played in the
#               terminal.
################################################################################

################################################################################
# Desc: Imports
import random as r
import sympy.ntheory as nt
import math
################################################################################

# This function starts the game
def play():
    pass

# This function determines if a win condition has been met
def win_condition():
    pass

# This function determines if a lose condition has been met
def lose_condition():
    pass

################################################################################
# Function:    playing_field()
# Description: Takes user input to determine the desired size and returns the
#              size and number of bombs
# Bugs:        No known bugs
################################################################################

def playing_field():
    square_playing_field = input("Playing Area: ")
    number_of_bombs = input("Number of bombs: ")
    while(int(number_of_bombs) >= int(square_playing_field)**2):
        print("Please enter number of bombs that is less than the size of the playing field: ")
        number_of_bombs = input("Number of bombs: ")
    print(f"You decided {square_playing_field}x{square_playing_field} with {number_of_bombs} bomb(s).")
    return [square_playing_field, number_of_bombs]

################################################################################
# Function:    create_playing_field(size, bombs)
# Description: Creates a playing field of desired size and the desired amount
#              of bombs
# Bugs: Can't create the maximum amount of bombs (Field size - 1)
################################################################################

def create_playing_field(size, bombs):
    bomb_count = 0
    position = []
    location = []
    rows_columns = 0
    for rows in range(0, int(size)):
        for columns in range(0, int(size)):
            box_value = r.randint(1, int(size)**2)
            rows_columns += 1
            if not nt.isprime(box_value) or bomb_count == int(bombs):
                print(rows_columns, end = ' ')
                position.append(0)
                location.append(rows_columns)
            else:
                # Just change what is printed and it should "mask" the value
                print(rows_columns, end = ' ')
                position.append('*')
                location.append(rows_columns)
                bomb_count += 1
        print()
    return position, location

################################################################################
# Function:    check_for_bombs(field)
# Description: Iterates through the field list and determines if the index is
#              either a bomb or a safe space. If it is a safe space, it tests
#              if the space is touching any bombs in the adjacent squares and if
#              it is, it adds one to the counter placed in the index to indicate
#              how many bombs it touches.
# Bugs:        If the bomb is in the last index, there is an IndexError
################################################################################

def check_for_bombs(field, row):
    i = 0
    # Need to expand for use outside of a 5 x 5 matrix
    while i < len(field):
        if field[i] == '*':
            # If it is the last item in the row
            if i == 0:
                # Check right of bomb
                if field[i+1] != '*':
                    field[i+1] += 1
                # Check below bomb
                if field[i + row] != '*':
                    field[i + row] += 1
                # Check lower right diagonal
                if field[i + row + 1] != '*':
                    field[i + row + 1] += 1
            elif i % (row - 1) == 0 and i != 0:
                # Check left of bomb
                if field[i-1] != '*':
                    field[i-1] += 1
                # Check below bomb
                if field[i + row] != '*':
                    field[i+row] += 1
                # Check above bomb
                if field[i - row] != '*':
                    field[i - row] += 1
                # Check lower left diagonal
                if field[i + row - 1] != '*':
                    field[i + row - 1] += 1
                # Check upper left diagonal
                if field[i - row- 1] != '*':
                    field[i - row- 1] += 1
                # However, if it is the first row
                if i == 4:
                    # Check left of bomb
                    if field[i-1] != '*':
                        field[i-1] += 1
                    # Check below bomb
                    if field[i + row] != '*':
                        field[i+row] += 1
                    # Check lower left diagonal
                    if field[i + row - 1] != '*':
                        field[i + row - 1] += 1
            # If it is the first item in the row
            elif i % row == 0:
                    # Check right of bomb
                    if field[i+1] != '*':
                        field[i+1] = 1
                    # Check below bomb
                    if field[i + row] != '*':
                        field[i+row] += 1
                    # Check above bomb
                    if field[i - row] != '*':
                        field[i - row] += 1
                    # Check lower right diagonal
                    if field[i + row + 1] != '*':
                        field[i + row + 1] += 1
                    # Check upper right diagonal
                    if field[i - row + 1] != '*':
                        field[i - row + 1] += 1
            # If it is in the top row
            elif i < row and i != 0:
                # Check right of bomb
                if field[i+1] != '*':
                    field[i+1] +=1
                # Check left of bomb
                if field[i-1] != '*':
                    field[i-1] += 1
                # Check below bomb
                if field[i + row] != '*':
                    field[i+row] += 1
                # Check lower right diagonal
                if field[i + row + 1] != '*':
                    field[i + row + 1] += 1
                # Check lower left diagonal
                if field[i + row - 1] != '*':
                    field[i + row - 1] += 1
            # If it is in the bottom row
            elif i > row**2 - row:
                # Check right of bomb
                if field[i+1] != '*':
                    field[i+1] += 1
                # Check left of bomb
                if field[i-1] != '*':
                    field[i-1] += 1
                # Check above bomb
                if field[i - row] != '*':
                    field[i - row] += 1
                # Check upper right diagonal
                if field[i - row + 1] != '*':
                    field[i - row + 1] += 1
                # Check upper left diagonal
                if field[i - row- 1] != '*':
                    field[i - row- 1] += 1
            # All other items
            else:
                # Check right of bomb
                if field[i+1] != '*':
                    field[i+1] += 1
                # Check left of bomb
                if field[i-1] != '*':
                    field[i-1] += 1
                # Check below bomb
                if field[i + row] != '*':
                    field[i+row] += 1
                # Check above bomb
                if field[i - row] != '*':
                    field[i - row] += 1
                # Check lower right diagonal
                if field[i + row + 1] != '*':
                    field[i + row + 1] += 1
                # Check upper right diagonal
                if field[i - row + 1] != '*':
                    field[i - row + 1] += 1
                # Check lower left diagonal
                if field[i + row - 1] != '*':
                    field[i + row - 1] += 1
                # Check upper left diagonal
                if field[i - row- 1] != '*':
                    field[i - row- 1] += 1
        i+=1
    return field

def check_location(lst):
    contents = lst[0]
    location = lst[1]
    for i in range(0, len(lst[0])):
        if lst[0][i] == '*':
            print('BOOM!')


square_playing_field = playing_field()
size_of_field = square_playing_field[0]
bombs_in_field = square_playing_field[1]
position = create_playing_field(size_of_field, bombs_in_field)
bomb_location = check_for_bombs(position[0], int(size_of_field))
print(bomb_location)
kaboom = check_location(position)

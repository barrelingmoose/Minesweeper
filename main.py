import random as r
import sympy.ntheory as nt

# This function starts the game
def play():
    pass

# This function determines if a win condition has been met
def win_condition():
    pass

# This function determines if a lose condition has been met
def lose_condition():
    pass

# Function to take user input to determine playing field size
def playing_field():
    square_playing_field = input("Playing Area: ")
    print(f"You decided {square_playing_field}x{square_playing_field}")
    return square_playing_field

# Function to create the playing field
def create_playing_field(size):
    for rows in range(0, int(size)):
        for columns in range(0, int(size)):
            box_value = r.randint(1, int(size)**2)
            # print(box_value, end = ' ')
            if not nt.isprime(box_value):
                print('#', end = ' ')
            else:
                print('*', end = ' ')
        print()

square_playing_field = playing_field()
create_playing_field(square_playing_field)

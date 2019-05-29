from room import Room
from player import Player
from os import system

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
system('cls')
print("\n\n*****************************************************************************")
print("**************** T H O R B E N ' S    D U N G E O N *************************")
print("*****************************************************************************\n")
print("""Welcome to Thorben's Dungeon!""")
new_name = input(f"Please enter your name > ")

p = Player(new_name, room["outside"])

input(f"If ye dare enter, {p.name} ... press enter > ")
system('cls')

playerOptions = {
    "n": "North",
    "e": "East",
    "s": "South",
    "w": "West",
    "q": "Quit"
}
selection = ""

# While we have not selected Quit
# +1 because we added quit
while selection != "q":

    print(p.current_room, "\n\n")

    selection = input(
        "### ACTIONS ###\nMove North: n\nMove East: e\nMove South: s\nMove West: w\nQuit Game: q\n> ")

    # error handler using try
    try:
        move_choice = f"you moved to the {playerOptions[selection]}\n"

        if selection == "n":
            p.current_room = p.current_room.n_to
            system("cls")
            print(move_choice)

        elif selection == "e":
            p.current_room = p.current_room.e_to
            system("cls")
            print(move_choice)

        elif selection == "s":
            p.current_room = p.current_room.s_to
            system("cls")
            print(move_choice)

        elif selection == "w":
            p.current_room = p.current_room.w_to
            system("cls")
            print(move_choice)

        else:
            print("GAME OVER\n\nThank you for playing!")
    except AttributeError:
        system("cls")
        print("There is no way through in that direction, please try again.\n")
    except KeyError:
        system("cls")
        print("Invalid selection. Please choose from the options provided\n")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

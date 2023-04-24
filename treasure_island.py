import random
import functions

# ASCII art of a pirate treasure box
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/
*******************************************************************************
''')

# Introduction to the game
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Define available directions
directions = ["left", "right"]

# Randomly choose the correct direction to reach the treasure
right_direction = random.choice(directions)

# Ask the user to choose a direction
direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").strip().lower()

# Check if the user chose the right direction
if direction == right_direction:
    # Ask the user if they want to wait for a boat or swim across a lake
    lake_decision = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait "
                          "for a boat. Type \"swim\" to swim across\n").strip().lower()
    # Call a function to handle the user's decision
    functions.cross_road(lake_decision)
    # Call a function to continue the game
    functions.house()

# If the user didn't choose the right direction, end the game
elif direction not in directions:
    print("You chose an invalid option. Game Over.")
else:
    print("You fell into a hole. Game Over.")

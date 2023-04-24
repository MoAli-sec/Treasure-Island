import random
import sys


def random_outcome():
    """
    This function returns a random outcome for the decision points in the game.
    """
    outcomes = ["win", "lose"]
    return random.choice(outcomes)


def cross_road(lake_decision):
    """
    This function handles the lake decision point.
    """
    if lake_decision == "wait":
        outcome = random_outcome()
        if outcome == "win":
            print("A boat arrives and takes you to the island. You are safe.")
        else:
            print("A boat arrives but, A strong storm came and the boat hit a giant wave and the boat sank with you."
                  " Game Over.")
            sys.exit()
    elif lake_decision == "swim":
        outcome = random_outcome()
        if outcome == "win":
            print("You successfully swim across the lake and arrive at the island.")
        else:
            print("You get attacked by an angry trout. Game Over.")
            sys.exit()
    else:
        print("You chose an invalid option. Game Over.")
        sys.exit()


def house():
    """
    This function handles the house decision point.
    """

    door_decision = input("You arrive at the island unharmed. There is a house with 3 doors. one red, one yellow "
                          "and one blue. Which color do you choose?\n").strip().lower()

    final_decision = ["fire", "beasts", "treasure"]
    fate = random.choice(final_decision)
    if door_decision == "red":
        if fate == "fire":
            print("It's a room full of fire. Game Over.")
        elif fate == "beasts":
            print("You entered a room of beasts. Game Over.")
        else:
            print("You found the treasure! You Win!")
    elif door_decision == "blue":
        if fate == "fire":
            print("It's a room full of fire. Game Over.")
        elif fate == "beasts":
            print("You entered a room of beasts. Game Over.")
        else:
            print("You found the treasure! You Win!")
    else:
        if fate == "fire":
            print("It's a room full of fire. Game Over.")
        elif fate == "beasts":
            print("You entered a room of beasts. Game Over.")
        else:
            print("You found the treasure! You Win!")

"""
A game for rock, paper, scissors
"""

import random
possible_actions = ["Rock🪨", "Paper📃", "Scissors✂️"]

actions = {1: "Rock🪨", 2:"Paper📃", 3:"Scissors✂️"}

computer_action = random.choice(possible_actions)


print("""
        Possible Values:
      1.Rock🪨
      2.Paper📃
      3.Scissors✂️
    """)


user_action = int(input("Enter Your Value : "))

map_user_action = actions[user_action]


if computer_action == map_user_action:
    print(f"Ohh! Its a tie..{computer_action}")

elif map_user_action == "Rock🪨":

    if computer_action == "Paper📃":
        print(f"You Lost..{computer_action}")
    else:
        print(f"You Win..{computer_action}")



elif map_user_action == "Paper📃":

    if computer_action == "Scissors✂️":
        print(f"You Lost..{computer_action}")
    else:
        print(f"You Win..{computer_action}")


elif map_user_action == "Scissors✂️":

    if computer_action == "Rock🪨":
        print(f"You Lost..{computer_action}")
    else:
        print(f"You Win..{computer_action}")










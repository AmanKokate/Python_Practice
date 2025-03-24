# user will get 5 chances
# computer will generate number 
# computer will give hints
# user will guess the number 

import random

chances = 5

print("""
        please select level of game...
        1. Easy
        2. Hard
        3. Extreme Hard
     """)
game_level = int(input("Enter Level: "))

if game_level == 1:
    computer_generated_number = random.randint(0, 50)
elif game_level == 2 :
    computer_generated_number = random.randint(0, 100)
else:
    computer_generated_number = random.randint(0 , 200)



computer_generated_number = random.randint(0, 100)

won = False

while chances :
    chances -= 1
    user_guess = int(input("Enter your guess: "))

    if user_guess == computer_generated_number:
        won = True
        print(f"congratulations! you guessed the number. Left {chances} chances")
        break

    elif user_guess > computer_generated_number:
        print(f"sorry! The number is less.Left {chances} chances")

    elif user_guess < computer_generated_number:
        print(f"Sorry! The number is greator. Left {chances} chances")


if not won:
    print(f"you lost better luck next time. The Number was{computer_generated_number}")


    

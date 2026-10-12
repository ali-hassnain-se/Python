# Simple Number Guessing Game

import random

# Play Function
def play_game():
    lucky_num=random.randint(1, 100)

    while True:
        user_num=int(input("Guess Your Lucky Number: "))
        
        if user_num==lucky_num:
            print("You Won. Game Over!!")
            break
        elif user_num<lucky_num:
            print("Too Low")
        else:
            print("Too High")

    print("Thank You! For Playing.")

# calling function
play_game()
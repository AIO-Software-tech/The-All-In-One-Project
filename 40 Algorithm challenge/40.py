#Write an algorithm for a game of your choice that:
#• Gives the user 3 lives at the start of the game.
#• Allows the user to play the game until their have no lives left.
#• They should move onto the next level for every 5 points they earn.
#• The game is complete when they receive 20 points.
#• At the end of the game it should tell the user which level they got up to

import random

points = 0
lives = 3
def level1(lives, points):
    while lives != 0:
        if points < 5:
            GuessesNum = random.randint(1, 2)
            print(GuessesNum)
            UserGuesses = int(input("Please Guesses a number between 1 and 2: "))
            if UserGuesses != GuessesNum:
                lives = lives - 1
                print("You lost a life. You have", lives, "left")
            elif UserGuesses == GuessesNum:
                points = points + 1
                print("You have:", points, "point")
                
        elif points < 10:
            GuessesNum = random.randint(1, 3)
            print(GuessesNum)
            UserGuesses = int(input("Please Guesses a number between 1 and 3: "))
            if UserGuesses != GuessesNum:
                lives = lives - 1
                print("You lost a life. You have", lives, "left")
            elif UserGuesses == GuessesNum:
                points = points + 1
                print("You have:", points, "point")

        elif points < 15:
            GuessesNum = random.randint(1, 4)
            print(GuessesNum)
            UserGuesses = int(input("Please Guesses a number between 1 and 4: "))
            if UserGuesses != GuessesNum:
                lives = lives - 1
                print("You lost a life. You have", lives, "left")
            elif UserGuesses == GuessesNum:
                points = points + 1
                print("You have:", points, "point")

        elif points < 20:
            GuessesNum = random.randint(1, 5)
            print(GuessesNum)
            UserGuesses = int(input("Please Guesses a number between 1 and 5: "))
            if UserGuesses != GuessesNum:
                lives = lives - 1
                print("You lost a life. You have", lives, "left")
            elif UserGuesses == GuessesNum:
                points = points + 1
                print("You have:", points, "point")

        elif points == 20:
            print("You Won")
            
    print("Game Over")

level1(lives, points)

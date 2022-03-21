import random

RPS = random.randrange(1,3)

YourRPS = input("Please enter rock paper or sisers: ")

if RPS == "1" and YourRPS == "rock":
    print("you win!")
elif RPS == "2" and YourRPS == "paper":
    print("you win!")
elif RPS == "3" and YourRPS == "sisers":
    print("you win!")
else:
    print("you lost")
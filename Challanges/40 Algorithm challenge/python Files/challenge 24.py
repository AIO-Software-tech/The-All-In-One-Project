#Challenge 24
#Create an algorithm that that:
#• Randomly generates the computer status ‘rock’ ‘paper’ or ‘scissors.’
#• Asks the user to input their status ‘rock’ ‘paper’ or ‘scissors.’
#• If the computer and user have the same status then output ‘Game Tied.’
#• If the computer generates ‘Rock’ and user generates ‘Scissors’ then output ‘Computer
#Wins’
#• If the computer generates ‘Paper’ and user generates ‘Rock’ then output ‘Computer Wins’
#• If the computer generates ‘Scissors’ and user generates ‘Paper’ then output ‘Computer
#Wins’
#Otherwise output ‘You Win!’

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
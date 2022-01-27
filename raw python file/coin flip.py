import random
import time

def menu():
    print("Menu")
    
def flip():
    amount = int(input("How many time do you want to flip the coin: "))
    if amount > 100:
        print('\033[1;31;40m Error #503 number is too large\033[0;37;40m')
        menu()
    else:
        for x in range (amount):
            side = random.randint(1, 1000000)
            if side == int(1000000):
                print("The coin landed on the side whats the chance")
            else:
                flip = random.randint(1, 2)
                if flip == int(1):
                    print("The coin landed on heads")
                    print(" ")
                    time.sleep(0.2)
                elif flip == int(2):
                    print("The coin landed on tails")
                    print(" ")
                    time.sleep(0.2)
        playAgain()

        

def playAgain():
    yes = "yes"
    Yes = "Yes"
    YES = "YES"
    no = "no"
    No = "No"
    NO = "NO"
    PlayAgin = str(input("Do you want to play again: "))
    if PlayAgin == str(yes):
        flip()
    elif PlayAgin == str(Yes):
        flip()
    elif PlayAgin == str(YES):
        flip()
    elif playAgain == str(no):
        menu()
    elif playAgain == str(No):
        menu()
    elif playAgain == str(NO):
        menu()

flip()

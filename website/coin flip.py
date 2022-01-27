import random


def flip():
    side = random.randint(1, 1000000)
    if side == "1000000":
        print("The coin landed on the side whats the chance")
    else:
        flip = random.randint(1, 2)
        if flip == "1":
            print("The coin landed on heads")
        elif flip == "2":
            print("The coin landed on tails")
    
    PlayAgin = input("Do you want to play again")
    if PlayAgin == "yes":
        flip()
    elif PlayAgin == "Yes":
        flip()
    elif PlayAgin == "YES":
        flip()
    elif PlayAgin == "no":
        menu()
    elif PlayAgin == "No":
        menu()
    elif PlayAgin == "NO":
        menu()
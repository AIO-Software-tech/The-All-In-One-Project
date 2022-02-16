import time

ride = 0

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    print(" ")
    print(" ")
    print('The ride is empty')
    count()

def count():
    ride = 0
    while ride < 8:
        rider = int(input("Please enter height in cm: "))

        if rider >= 140:
            print("Please ride")
            ride = ride + 1
        elif rider >=120 and rider <140 :
            adult = input("Are you an adult y/n: ")
            if adult == "y":
                print("Please both ride!")
                ride = ride +2
            else:
                print("No ride!")
        else:
            print("No ride!")
    print("The ride is full please wait")
    print(" ")
    countdown(int(120))

count()
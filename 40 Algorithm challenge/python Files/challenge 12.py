#Challenge 12
#Write an algorithm that:
#	•Generates a random number between 1 and 10.
#	•It must then ask the user to guess this number. 
#	•If they guess it correctly it should display ‘Correct’
#	•Otherwise, display ‘Not what I was thinking’

import random

num = random.randint(1, 10)
Unum = float(input("please enter a number: "))

if Unum == num:
    print("Correct")
else:
    print("Not what i was thinking")
    print(str(num) + " is wat i got")

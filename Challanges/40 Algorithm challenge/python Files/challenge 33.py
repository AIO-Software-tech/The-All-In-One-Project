#Challenge 33
#Write an algorithm that:
#   • Ask the user to input how many GCSE’s they have.
#   • They should then be allowed to enter a result for each GCSE grade.
#   • The computer should work out how many points they have got (9=9, 8=8, 7=7 etc).
#   • If their score is 40 or over it should output ‘You can go to the sixth form’
#   • If they their score between 35 and 39 it should output ‘A discussion is needed’
#   • Otherwise it should say ‘Sorry not enough points.’

Sum_Of_Entries = 0
Amount_Of_Entries = int(input("How Many GCSE's Do You Have?: "))

for i in range(Amount_Of_Entries):
    Sum_Of_Entries += int(input(f"Please enter the points you got ({i+1}/{Amount_Of_Entries}): "))

Average_Num = round(Sum_Of_Entries/Amount_Of_Entries, 2)

if Average_Num >= 40:
    print("Welcome To Sixth Form, Friend.")
elif Average_Num > 35 and Average_Num < 39:
    print("A Discussion Is Needed.")
else:
    print("Sorry Not Enough Points To Enter Sixth Form.")
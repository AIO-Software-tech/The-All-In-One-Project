#Challenge 22
#Write an algorithm that:
#   Asks the user to input how many marks they got on a test.
#   It should then convert this to a grade between 1 to 9 using the table below and then output the grade to the user. 
#   If they have not scored enough to be given a grade than a ‘U’ grade must be output.

mark = int(imput("how many marks did you get on the test"))

if mark >= 10:
    print("1")

elif mark >= 20:
    print("2")

elif mark >= 30:
    print("3")
    
elif mark >= 40:
    print("4")

elif mark >= 50:
    print("5")

elif mark >= 60:
    print("6")

elif mark >= 70:
    print("7")   

elif mark >= 80:
    print("8")

elif mark >= 90:
    print("9")
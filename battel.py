import time

print("0 1 2 3 4 5 6 7 8 9 10")
print("1 #   # # #")
print("2 #                 #")
print("3 #         #")
print("4 #         #")
print("5 #     # # # #")
print("6")
print("7                    #")
print("8                    #")
print("9       #")
print("10")

def pickPos():
    Carrier1Pos1 = input("Please enter postion 1 of your Carrier (e.g. 1,a): ")
    Carrier1Pos2 = input("Please enter postion 2 of your Carrier (e.g. 1,e): ")
    if Carrier1Pos1 == "1,a" or Carrier1Pos1 == "1,b" or Carrier1Pos1 == "1,c" or Carrier1Pos1 == "1,d" or Carrier1Pos1 == "1,e" or Carrier1Pos1 == "1,f" or Carrier1Pos1 == "1,g" or Carrier1Pos1 == "1,h" or Carrier1Pos1 == "1,i" or Carrier1Pos1 == "1,j":
        if Carrier1Pos2 == "5,a" or Carrier1Pos2 == "5,b" or Carrier1Pos2 == "5,c" or Carrier1Pos2 == "5,d" or Carrier1Pos2 == "5,e" or Carrier1Pos2 == "5,f" or Carrier1Pos2 == "5,g" or Carrier1Pos2 == "5,h" or Carrier1Pos2 == "5,i" or Carrier1Pos2 == "5,j":
            print("Valid")
        else:
            print("error")
    
    elif Carrier1Pos1 == "2,a" or Carrier1Pos1 == "2,b" or Carrier1Pos1 == "2,c" or Carrier1Pos1 == "2,d" or Carrier1Pos1 == "2,e" or Carrier1Pos1 == "2,f" or Carrier1Pos1 == "2,g" or Carrier1Pos1 == "2,h" or Carrier1Pos1 == "2,i" or Carrier1Pos1 == "2,j":
        if Carrier1Pos2 == "6,a" or Carrier1Pos2 == "6,b" or Carrier1Pos2 == "6,c" or Carrier1Pos2 == "6,d" or Carrier1Pos2 == "6,e" or Carrier1Pos2 == "6,f" or Carrier1Pos2 == "6,g" or Carrier1Pos2 == "6,h" or Carrier1Pos2 == "6,i" or Carrier1Pos2 == "6,j":
            print("Valid")
        else:
            print("error")
    elif Carrier1Pos1 == "3,a" or Carrier1Pos1 == "3,b" or Carrier1Pos1 == "3,c" or Carrier1Pos1 == "3,d" or Carrier1Pos1 == "3,e" or Carrier1Pos1 == "3,f" or Carrier1Pos1 == "3,g" or Carrier1Pos1 == "3,h" or Carrier1Pos1 == "3,i" or Carrier1Pos1 == "3,j":
        if Carrier1Pos2 == "5,a" or Carrier1Pos2 == "5,b" or Carrier1Pos2 == "5,c" or Carrier1Pos2 == "5,d" or Carrier1Pos2 == "5,e" or Carrier1Pos2 == "5,f" or Carrier1Pos2 == "5,g" or Carrier1Pos2 == "5,h" or Carrier1Pos2 == "5,i" or Carrier1Pos2 == "5,j":
            print("Valid")
        else:
            print("error")
    elif Carrier1Pos1 == "4,a" or Carrier1Pos1 == "4,b" or Carrier1Pos1 == "4,c" or Carrier1Pos1 == "4,d" or Carrier1Pos1 == "4,e" or Carrier1Pos1 == "4,f" or Carrier1Pos1 == "4,g" or Carrier1Pos1 == "4,h" or Carrier1Pos1 == "4,i" or Carrier1Pos1 == "4,j":
        if Carrier1Pos2 == "5,a" or Carrier1Pos2 == "5,b" or Carrier1Pos2 == "5,c" or Carrier1Pos2 == "5,d" or Carrier1Pos2 == "5,e" or Carrier1Pos2 == "5,f" or Carrier1Pos2 == "5,g" or Carrier1Pos2 == "5,h" or Carrier1Pos2 == "5,i" or Carrier1Pos2 == "5,j":
            print("Valid")
        else:
            print("error")
    elif Carrier1Pos1 == "5,a" or Carrier1Pos1 == "5,b" or Carrier1Pos1 == "5,c" or Carrier1Pos1 == "5,d" or Carrier1Pos1 == "5,e" or Carrier1Pos1 == "5,f" or Carrier1Pos1 == "5,g" or Carrier1Pos1 == "5,h" or Carrier1Pos1 == "5,i" or Carrier1Pos1 == "5,j":
        if Carrier1Pos2 == "5,a" or Carrier1Pos2 == "5,b" or Carrier1Pos2 == "5,c" or Carrier1Pos2 == "5,d" or Carrier1Pos2 == "5,e" or Carrier1Pos2 == "5,f" or Carrier1Pos2 == "5,g" or Carrier1Pos2 == "5,h" or Carrier1Pos2 == "5,i" or Carrier1Pos2 == "5,j":
            print("Valid")
        else:
            print("error")
    elif Carrier1Pos1 == "6,a" or Carrier1Pos1 == "6,b" or Carrier1Pos1 == "6,c" or Carrier1Pos1 == "6,d" or Carrier1Pos1 == "6,e" or Carrier1Pos1 == "6,f" or Carrier1Pos1 == "6,g" or Carrier1Pos1 == "6,h" or Carrier1Pos1 == "6,i" or Carrier1Pos1 == "6,j":
        if Carrier1Pos2 == "5,a" or Carrier1Pos2 == "5,b" or Carrier1Pos2 == "5,c" or Carrier1Pos2 == "5,d" or Carrier1Pos2 == "5,e" or Carrier1Pos2 == "5,f" or Carrier1Pos2 == "5,g" or Carrier1Pos2 == "5,h" or Carrier1Pos2 == "5,i" or Carrier1Pos2 == "5,j":
            print("Valid")
        else:
            print("error")
    elif Carrier1Pos1 == "7,a" or Carrier1Pos1 == "7,b" or Carrier1Pos1 == "7,c" or Carrier1Pos1 == "7,d" or Carrier1Pos1 == "7,e" or Carrier1Pos1 == "7,f" or Carrier1Pos1 == "7,g" or Carrier1Pos1 == "7,h" or Carrier1Pos1 == "7,i" or Carrier1Pos1 == "7,j":
        if Carrier1Pos2 == "5,a" or Carrier1Pos2 == "5,b" or Carrier1Pos2 == "5,c" or Carrier1Pos2 == "5,d" or Carrier1Pos2 == "5,e" or Carrier1Pos2 == "5,f" or Carrier1Pos2 == "5,g" or Carrier1Pos2 == "5,h" or Carrier1Pos2 == "5,i" or Carrier1Pos2 == "5,j":
            print("Valid")
        else:
            print("error")
    elif Carrier1Pos1 == "8,a" or Carrier1Pos1 == "8,b" or Carrier1Pos1 == "8,c" or Carrier1Pos1 == "8,d" or Carrier1Pos1 == "8,e" or Carrier1Pos1 == "8,f" or Carrier1Pos1 == "8,g" or Carrier1Pos1 == "8,h" or Carrier1Pos1 == "8,i" or Carrier1Pos1 == "8,j":
        if Carrier1Pos2 == "5,a" or Carrier1Pos2 == "5,b" or Carrier1Pos2 == "5,c" or Carrier1Pos2 == "5,d" or Carrier1Pos2 == "5,e" or Carrier1Pos2 == "5,f" or Carrier1Pos2 == "5,g" or Carrier1Pos2 == "5,h" or Carrier1Pos2 == "5,i" or Carrier1Pos2 == "5,j":
            print("Valid")
        else:
            print("error")
    elif Carrier1Pos1 == "9,a" or Carrier1Pos1 == "9,b" or Carrier1Pos1 == "9,c" or Carrier1Pos1 == "9,d" or Carrier1Pos1 == "9,e" or Carrier1Pos1 == "9,f" or Carrier1Pos1 == "9,g" or Carrier1Pos1 == "9,h" or Carrier1Pos1 == "9,i" or Carrier1Pos1 == "9,j":
        if Carrier1Pos2 == "5,a" or Carrier1Pos2 == "5,b" or Carrier1Pos2 == "5,c" or Carrier1Pos2 == "5,d" or Carrier1Pos2 == "5,e" or Carrier1Pos2 == "5,f" or Carrier1Pos2 == "5,g" or Carrier1Pos2 == "5,h" or Carrier1Pos2 == "5,i" or Carrier1Pos2 == "5,j":
            print("Valid")
        else:
            print("error")
    elif Carrier1Pos1 == "10,a" or Carrier1Pos1 == "10,b" or Carrier1Pos1 == "10,c" or Carrier1Pos1 == "10,d" or Carrier1Pos1 == "10,e" or Carrier1Pos1 == "10,f" or Carrier1Pos1 == "10,g" or Carrier1Pos1 == "10,h" or Carrier1Pos1 == "10,i" or Carrier1Pos1 == "10,j":
        if Carrier1Pos2 == "5,a" or Carrier1Pos2 == "5,b" or Carrier1Pos2 == "5,c" or Carrier1Pos2 == "5,d" or Carrier1Pos2 == "5,e" or Carrier1Pos2 == "5,f" or Carrier1Pos2 == "5,g" or Carrier1Pos2 == "5,h" or Carrier1Pos2 == "5,i" or Carrier1Pos2 == "5,j":
            print("Valid")
        else:
            print("error")

    
pickPos()

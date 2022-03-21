#Challenge 23
#Create an algorithm that will:
#   •Allow the user to input how much money they want to change to coins. 
#   •Select which coin they want to convert the money into £1, 50p, 20p, 10p, 5p, 2p ,p
#   •Calculate how many of each coin will be given in.

howToCoin = input("Please enter the amount you what to convert to coins: ")

howToCoin = float(howToCoin)
if howToCoin >= 0.99:
    howToCoin = int(howToCoin)
    print("You will get £" + str(howToCoin))
    print("We dont get and thing bellow 0.99")

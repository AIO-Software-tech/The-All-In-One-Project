#Challenge 8
#The program asks the user to input how many minutes and texts they have used in the
#last month and then outputs the total cost of the bill. This is calculated by
#working out:
#   •The total cost of the minutes (at £0.10 per minute) and....
#   •Adding this to the total cost of the texts (at £0.05 per text) and....
#   •Adding on an additional monthly charge of £10.00.

mins = int(input("please enter how many call minute you have used: "))
texts = int(input("please enter how many texts you have send: "))

print("£" + str(mins * 0.10))
print("£" + str(texts * 0.05))

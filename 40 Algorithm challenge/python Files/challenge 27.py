#Challenge 27
#The cost of a day-time journey is £3 for the first kilometre and £2 for every kilometre after that.
#If there are five of more passengers in the taxi, and extra 50% is added to the charge.
#Write an algorithm to calculate the cost of a day-time journey.
#Your algorithm should:
#   • Allow the number of passengers and he distance of the journey to be input as whole numbers,
#   • Calculate the cost of the journey,
#   • Output the cost that has been calcuated.

DisTraveled = float(input("How Far Have You Traveled?: "))
NumOfPasengers = int(input("How Many Passengers Are There?: "))

if DisTraveled <= 1 and NumOfPasengers <= 4:
    print("This Ride Will Cost You: £3")

elif DisTraveled <= 1 and NumOfPasengers >= 5:
    print("This Ride Will Cost You:  £4.50")
elif DisTraveled > 1 and NumOfPasengers > 4:
    MilePrice = DisTraveled - 1
    SecondMilePrice = MilePrice * 3 + 2
    ThirdMilePrice = SecondMilePrice / NumOfPasengers
    NumOfPasengers1 = NumOfPasengers - 1
    Price = ThirdMilePrice * NumOfPasengers1 + ThirdMilePrice
    print("Your Trip Costs: " + str(Price))
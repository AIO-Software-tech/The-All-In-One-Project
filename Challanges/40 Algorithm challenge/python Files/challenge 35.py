#Challenge 35
#Write an algorithm that:
#   • Asks the user to input many cars are available for a trip.
#   • Asks the user to input how many people are going on the trip.
#   • If there are enough seats it should output ‘We have enough seats’
#   • If there are not enough seats it calculates how many extra cars are needed and then output ‘Another x cars are needed’ with x being the number of cars.
#NOTE: Assume you can fit FIVE people in each car.

Seats_In_A_Car = 5

Amount_Of_Cars = int(input("How many cars are available for the trip?: "))
Amount_Of_People = int(input("How many people will go to the trip?: "))
Amount_Of_Seats = Amount_Of_Cars * Seats_In_A_Car

if Amount_Of_People <= Amount_Of_Seats:
    print("Looks good. We have enough cars!")
else:
    Amount_Of_People_Over = Amount_Of_People - Amount_Of_Seats
    Amount_Of_Needed_Cars = round(Amount_Of_People_Over / Seats_In_A_Car + 0.5)
    print(f"Not enough cars. Get at least {Amount_Of_Needed_Cars} more car(s).")
#Challenge 29
#The wages earned by a worker is either £2 for every teddy bear the have made or £5 for every hour they have worked, whichever is larger.
#Write an algorithm that:
#   • allows the user to input the number of teddy bears made and the number of hours worked
#   • calculates the wages for the number of teddy bears made
#   • calculates the wages for the number of hours worked
#   • outputs the larger of the two results.

PRICE_PER_TEDDY = 2 # bri'ish pounds
PRICE_PER_HOUR = 5 # bri'ish pounds

amount_of_teddy = int(input("Input the amount of teddy bears made: "))
amount_of_hours = int(input("Input the amount of hours worked: "))

wage_for_teddy = amount_of_teddy * PRICE_PER_TEDDY
wage_for_hours = amount_of_hours * PRICE_PER_HOUR

end_wage = 0

if wage_for_teddy > wage_for_hours:
    end_wage = wage_for_teddy
else:
    end_wage = wage_for_hours

print(f"You earned exactly {end_wage} briish pounds.")
input()

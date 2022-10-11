#Challenge 21
#A local swimming centre offers the following discounts: 
#   1.Members who areaged between 13 and 15 receive a 30% discount.
#   2.Members who are aged between 16 and 17 receive a 20% discount.
#   3.Members who are aged 50 and over receive a 40% discount.4.
#   All other members receive no discount. 

print("Find out how much you can be discounted")
age = int(input("Please enter you age: "))

if age == 13:
    print("You get a 30 persent discount")

elif age == 14 :
    print("You get a 30 persent discount")

elif age == 15 :
    print("You get a 30 persent discount")

elif age == 16 :
    print("You get a 20 persent discount")

elif age == 17 :
    print("You get a 20 persent discount")

elif age > 50:
    print("You get a 40 persent discount")

else:
    print("LOL no discount for you")    
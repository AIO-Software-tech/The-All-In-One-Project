#Challenge 20
#MyHotPizza company have developed a new loyalty reward system for customers.
#Customers are automatically sent a reward card if they order more than 20 pizzas in a year.
#Write an algorithm that goes through the customer orders, and where needed, sends customers a loyalty card if they do not already have one.
#If they have not ordered enough pizzas, then it removes them from the card list.

def discountJ():
    print("Large = 5")
    print("Medium = 6")
    print("Small = 1")
    print("Card = No")
    l = 5
    m = 6
    s = 1
    c = "no"
    if l + m + s >= 20:
        print("You get a discount")
    else:
        print("You are not eleragable for a discount. Sorry :(")

def discountO():
    print("Large = 1")
    print("Medium = 5")
    print("Small = 34")
    print("Card = Yes")
    l = 1
    m = 5
    s = 34
    c = "yes"
    if l + m + s >= 20:
        print("You get a discount")
    else:
        print("You are not eleragable for a discount. Sorry :(")

def discountP():
    print("Large = 10")
    print("Medium = 12")
    print("Small = 3")
    print("Card = Yes")
    l = 10
    m = 12
    s = 3
    c = "yes"
    if l + m + s >= 20:
        print("You get a discount")
    else:
        print("You are not eleragable for a discount. Sorry :(")
        
name = input("Please enter your name: ")
if name == "Ollie":
    discountO()
elif name == "John":
    discountJ()
elif name == "Philep":
    discountP()
else:
    print("You are not eleragable for a discount. Sorry :(")


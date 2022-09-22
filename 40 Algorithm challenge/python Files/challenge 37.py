#Challenge 37
#A free drinks machine in an office provides 20 different drinks.
#The machine has a small keypad with keys 0 to 9, OK and CANCEL.
#It also has a small LCD screen, which can display a short message.
#To get a drink, users select an item number between 1 and 20 with the keypad and confirm their choice by pressing OK.
#If they make a mistake, they can press the CANCEL button and start again.
#If the selection is valid and the drink is available it dispenses the drink. The display screen is used to show suitable short messages throughout the process.
import sys
AMOUNT_OF_DRINKS = 20

def main():
    Drink_Choice = int(input("Hello There What Would You Like To Drink? (1 - 20): "))
    if Drink_Choice > 20 or Drink_Choice < 1:
        print("That's not A Drink We Serve.")
        return 1
    confirm = input("Are you sure? (Yes, No Or Something Else): ")
    if confirm == "No":
        print("Then Why Did You Ask For It?")
    elif confirm == "Something Else":
        return 1
    elif confirm == "Yes":
        print(f"Here's Your Drink, A Number {Drink_Choice}")
    elif confirm == "Cancel":
        print("Well Come Back To Me If You Need One.")
    return 0

while True:
    result = main()
    if result == 0:
        break
# Assignment 1
# Program name: Level 3 Challange 46 Quiz incomplete
# This program asks three quiz questions, and cores the answers

#(Correct andswers are: hummingbird, False, bullfrog)

score = 0

answer = "a"
if answer == "a" or answer == "A":
    print("Correct")
else:
    print("Wrong")

answer = input("\nYou can get warts from tuching a toad - \n\ True (T) or False (F)? ")
if answer == "F" or answer == "f":
    print("Correct")
else:
    print("False")

print("1. Balance enquiry")
print("2. Mini statement")
print("3. Fast cash\n")

choice = int(input("Please select somthing from the options above: "))
if choice == "1":
    print("Option 1 selected: balance printed")

elif choice == "2":
    print("Option 2 selected: Mini statement")

elif choice == "3":
    print("Option 3 selected: Fast cash")

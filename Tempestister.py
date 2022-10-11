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

answer = input("\nYou Can Get Warts From Touching A Toad - \n\ True (T) or False (F)? ")
if answer == "F" or answer == "f":
    print("Correct")
else:
    print("False")

print("1. Balance Enquiry")
print("2. Mini Statement")
print("3. Fast Cash\n")

choice = int(input("Please Select Somthing From The Options Above: "))
if choice == "1":
    print("Option 1 Selected: Balance Printed")

elif choice == "2":
    print("Option 2 Selected: Mini Statement")

elif choice == "3":
    print("Option 3 Selected: Fast Sash")


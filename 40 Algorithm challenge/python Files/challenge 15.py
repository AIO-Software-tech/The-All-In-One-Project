#Challenge 15
#Write a program that:
#	•Asks the user to name one of the Olympic Values (Respect, Excellence and Friendship)
#	•If they correctly name one, output 'That’s correct‘
#	•Otherwise outputs ‘Incorrect’

Olympic = input("Please enter one of the Olympic Values: ")

if Olympic == "Respect" or "Excellence" or "Friendship":
	print("That’s correct")
else:
	print("Incorrect")



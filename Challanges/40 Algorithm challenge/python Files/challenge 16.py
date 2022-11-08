#Challenge 16
#Write an algorithm that:
#	•Asks the user how long on average they spend watching TV each day.
#	•If it is less than 2 hours, outputs ‘That should be ok’
#	•If it is between 2 and 4 hours, outputs ‘That will rot your brain’
#	•Otherwise outputs “That is too much TV”

time = input("How long do you watch tv for in minuest: ")

if time < 120:
	print('That should be ok')
elif time < 120 and time > 240:
	print("That will rot your brain")
elif time > 240:
	print("That is too mcuh")

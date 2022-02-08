#Challenge 11
#The program asks the user to input two numbers.
#It will then outputthe larger of these two numbers.

num1 = int(input("please enter a number: "))
num2 = int(input("please enter a second number: "))

if num1 > num2:
	print("Num1 is bigger")
elif num2 > num1:
	print("Num2 is bigger")
else:
	print("there the same")

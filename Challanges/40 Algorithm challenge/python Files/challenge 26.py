#Challenge 26
#A dog that is 5 years old is equivalent to a 42 year old human. Ashok is writing a program which
#converts the age of the dog to the equivalent age for a human.
#The program uses the following method:
#• The user inputs age of the dog in years
#• If the age is 2 or less, the human equivalent is 12 times the age
#• If the age is more hen 2, the human equivalent id 24 for the first 2 years, plus 6 for every
#additional year.
#Write an algorithm to calculate and output the human equivalent of the age of the dog using the
#method described.

DogAge = float(input("Please enter your dog's age: "))

if DogAge <= 2:
	FinalDogAge = DogAge * 12
	print("Your dog is "+ str(FinalDogAge) + " Years old")
elif DogAge > 2:
	FinalDogAge = DogAge * 12 + 6
	print("Your dog is "+ str(FinalDogAge) + " Years old")
#Challenge 25
#SpeedyClub Runners is a local sports club, who organise a 5k race every year.
#The results of the race are stored in a record structure (called RaceFile) as follows:
#RunnerNumber Name AgeCatagory Club?
#44325 Wilburforce, Emily U18 SpeedyClub
#543 Chan, Zhu Snr
#2425 Patel, Aisha Vet
#5552 Ewards, Craig Snr LighteningFast
#Runners
#Produce an algorithm that counts the number of runners in each Age category for the race

print("Age catagory= Under 18 = U18")
print("Age catagory= 62 or Older = Snr")
print("Age catagory= If your a veteran = Vet")

print( )

AgeCat = input("Please enter your age catagory: ")
if AgeCat == "U18":
    print("You are in: Speedy Club")
elif AgeCat == "Vet":
    print("You are in: Veteran Club")
elif AgeCat == "Snr":
    print("You are in: Lightening fast runner")
else:
  print("lol noob")
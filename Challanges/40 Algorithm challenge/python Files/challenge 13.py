#Challenge 13
#A company calculates holiday allowance for employees.
#The company gives each employees 28 days holiday each year.
#Holidays are awarded based on the following rules:
#1.Full time employees who work 5 days a week get 28 days holiday a year
#2.Part time employees get a proportion of holiday allowance based on how many days
#they work, e.g. An employee who works 1 day a week would only get 1/5 of the
#holidays allowed.

yes = "yes"
no = "no"

FullOrNot = input("Are you a full time employee: ")
if FullOrNot == yes:
    print("You have 28 days")
elif FullOrNot == no:

how = int(input("How many days a do you work: "))
    days = 28/how
    print("you have " + str(round(days)))

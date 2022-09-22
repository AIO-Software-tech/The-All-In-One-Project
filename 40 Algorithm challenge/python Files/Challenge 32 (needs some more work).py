#Challenge 32
#Norma would like to invest her savings in a bank account that generates the most money.
#She would like a program that will allow her to:
#   • Enter the amount of money she wants to save.
#   • Input the number of bank accounts she wants to compare.
#   • Enter the interest rate for each account.
#   • The interest is calculated by dividing the money to be saved by 100 and then multiplying this by the interest rate.
#   • The total is calculated by adding the money to be saved to the interest and then outputted.
#   • The program should repeat this for all bank accounts. 

MoneySaved = int(input("How Much Money Do You Want To Save?: "))
BankAccounts = int(input("How Much Bank Accounts Do You Want To Compare?: "))
InterestRate = int(input("How Much Is The Interest Rate For Each Account?: "))


Interest = MoneySaved / 100

print(Interest)
#Challenge 31
#The student is writing an algorithm to solve a problem.
#   • The user will provide a series of numbers, representing the weights in grams of individual fruits.
#   • The weights are always whole positive numbers.
#   • The number of weights to be entered will also be provided by the user.
#   • The solution should calculate and report the mean weight of the fruits to two decimal places.

sum_of_weights = 0
amount_of_entries = int(input("How many weights do you want to enter?: "))

for i in range(amount_of_entries):
    sum_of_weights += int(input(f"Enter weight {i+1}: "))

print(round(sum_of_weights/amount_of_entries, 2))
input()
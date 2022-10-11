#Challenge 39
#A primary school teacher wants a computer program to test the basic arithmetic skills of her students.
#The program should generate a quiz consisting of a series of random questions, using in each case any two numbers and addition, subtraction and multiplication.
#The system should ask student’s name, then ask 10 questions, output if the answer to each question is correct or not and produce a final score out of 10.
#Scores from the quiz should be stored and added to when a student takes a new quiz.
#Write an algorithm for the process described above. 

score = 0
amount_of_quizzes = 0
name = False
import random

def main():
    global name
    global score
    global amount_of_quizzes

    if not name:
        name = input("What's Your name?: ")
    print(f"Welcome, {name}")
    if score:
        print(f"Your Score Is {score}/{amount_of_quizzes}.")
    print("Please Answer These 10 Questions.")
    
    for i in range(10):
        amount_of_quizzes += 1
        random_sign = random.choice(["+", "-", "*"])
        random_problem = str(random.randrange(100)) + random_sign + str(random.randrange(100))
        actual_answer = eval(random_problem)
        user_answer = int(input(f"Question {i+1}: {random_problem}\nAnswer: "))
        if actual_answer == user_answer:
            print("You're Right!\n")
            score += 1
        else:
            print(f"Wrong, The Correct Answer is {actual_answer}\n")

    pass

while True:
    result = main()
    if result == 0:
        break
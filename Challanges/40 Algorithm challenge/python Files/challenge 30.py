#Challenge 30
#An isosceles triangle is a triangle that has at least two equal sides. The diagram below shows examples of isosceles triangles.
#In each diagram the marked sides are equal.
#Write an algorithm for a computer program that determines whether a triangle in an isosceles triangle.
#   • The user inputs the lengths of the three sides as Length 1, Length 2 and Length 3
#   • If any two side have the same length the program outputs “Isosceles”
#   • Otherwise the program outputs “Not Isosceles”

A = int(input("What Is The Length Of The First Side ?: "))
B = int(input("What Is The Length Of The Second Side ?: "))
C = int(input("What Is The Length Of The Third Side ?: "))

if A == B or A == C or B == C:
    print("Isosceles")
    
else:
    print("Not Isosceles")
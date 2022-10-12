# Challenge 1
if 10 * 7 == 70:
    print("True")
else:
    print("False")
    
# Challenge 2
if "John" != "JOHN":
    print("True")
else:
    print("False")

# Challenge 3
if 6 >= 2*4 and 28 <= 7*4:
    print("True")
else:
    print("False")

# Challenge 4
y = -1
x = -1
if x < 0 and y < 0:
    print("True")
else:
    print("False")

# Challenge 5
a = 0
b = 1
if a == 0 or b == 0:
    print("True")
else:
    print("False")

# Challenge 6
a = 24/8
b = 24+8
print(a==b)

# Challange 7
if (237//17)+0.941176470588236 == 237/17:
    print("True")
else:
    print("False")

# Challange 8
print((10 == 5*2) and (45 != 9*5))

# Challange 9
print((6*3 >= 9*2) and (30//7 == 2))

# Challange 10
right = float(input("Enter The Weight On The Right: "))
left = float(input("Enter The Weight On The Left: "))

print(left == right)

# Challange 11
length = float(input("Enter The length: "))
width = float(input("Enter The Width: "))

print(length == width)

# Challange 12
restingFor20Min = input("Have You Been Resting For 20 Mins? yes/no: ")
if restingFor20Min == "yes" or restingFor20Min == "Yes" or restingFor20Min == "YES" or restingFor20Min == "y" or restingFor20Min == "Y":
    restingRate = input("Is Your Resting Rate Between 60 And 100? yes/no: ")
    if restingRate == "yes" or restingRate == "Yes" or restingRate == "YES" or restingRate == "y" or restingRate == "Y":
        print("Your Heart Rate Is Within The Exoected Rage")
    else:
        print("Your Heart Rate Is Not Within The Exoected Rage You May Need To Seak Advice From 111")
else:
    print("Please Try Again Later")
#elif
num = int(input("Enter a number:"))
if(num<0):
    print("Number is negative")
elif(num>0):
    print("Number is positive")
else:
    print("Number is zero")

marks = int(input("Enter your marks between(0 to 100): "))
if marks < 0 or marks > 100:
    print("Invalid Marks!")
elif marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
elif marks >= 60 and marks < 70:
    print("Grade D")
elif marks >= 50 and marks < 60:
    print("Grade E")
else:
    print("You fail!")
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

#Largest three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 > num2 and num1 > num3:
    print("First number is greater than both")
if num2 > num1 and num2> num3:
    print("Second number is greater than both")
if num3 > num1 and num3 > num2:
    print("Third number is greater than both")
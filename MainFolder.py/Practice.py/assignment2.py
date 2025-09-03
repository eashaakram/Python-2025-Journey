#Problem 1: Take 3 numbers from user and print the smallest.
#Take input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
#check which number is smaller
if num1 < num2 and num1 < num3:
  print(f"First number {num1} is smallest number")
elif num2 < num1 and num2 < num3:
  print(f"Second number {num2} is smallest number")
else:
  print(f"Third number {num3} is smallest number")

#Problem 2: Take the year as input (e.g: 2025) and check whether the year is leap or not
#Take year as input
year = int(input("Enter any year: "))
#Check if year is leap or not
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(f"Yes, {year} is a leap year!")
else:
  print(f"No, {year} is not a leap year!")

'''Poblem 3: Take electricity units and calculate bill:
(units) 1–100 →  (Rs.) 10 per unit
(units) 101–200 →   (rRs.) 15 per unit
(units) above 200 →(  Rs.)  20 per unit'''
#Take units as input
unit = int(input("Enter electricity units:"))
#Calculate
while unit < 1:
  unit = int(input("Invalid input.\nPlease enter positive number start from One!"))
if unit >=1 and unit <= 100:
  bill = unit * 10
  print(f"Price of one unit is 10\nThe bill is: {bill} PKR")
elif unit >= 101 and unit <= 200:
  bill = unit * 15
  print(f"Price of one unit is 15\nThe bill is: {bill} PKR")
else:
  bill = unit * 20
  print(f"Price of one unit is 20\nThe bill is: {bill} PKR")

#Problem 4: Take a string from the user, then check whether the user actually entered something or left it blank.
#Take string input
text = input("Enter Anything: ")
#Check
if text == "":
  print("You did't enter anything!")
else:
  print(f"You entered: {text}")


'''Problem 5: Take a number from the user as input and check whether the number is positive, negative, or zero.
If the number is positive:
Determine whether it is even or odd.
If even:
Check whether it is divisible by 4 and divisible by 12.
If yes, add 10 to the number and print the updated value.
If odd:
Multiply the number by 3 and print the updated value.
Then check whether the new value is greater than 30 and print the result.
If the number is negative:
Determine whether it is even or odd.
If even:
Check whether it is less than -10 or greater than or equal to -10 and print the result.
If odd:
Multiply the number by 2 and print the updated value.
If the number is zero, simply print: "The number is zero".
Note: Print the number’s value and all intermediate results at each step.
'''
#Taking input from user
num = int(input("Enter number: "))
#Check number +ve, -ve or zero
print("Check number is positive, negative or zero")
if num == 0: #if zero
  print(f"{num}: Zero")
elif num > 0: #if positive
  print(f"{num}: Positive")
  print("Check Even or Odd")
  if num % 2 == 0: #if even
    print(f"{num}: Even")
    if (num % 4 == 0 and num % 12 == 0): #if divisible by 4 and 12
      num += 10
      print(f"Updated Value: {num}")
    else:
      print(f"{num}: Not divisible by 4 and 12")
  else: #odd
    print(f"{num}: Odd")
    num *= 3
    print(f"Updated Value: {num}")
    if num > 30: #check new number > or < 30
      print(f"{num}: Greater than 30")
    else:
      print(f"{num}: Less than 30")
else: #if negative
  print(f"{num}: Negative")
  print("Check Even or Odd")
  if num % 2 == 0: #if even
    print(f"{num}: Even")
    if num < -10: #less than -10
      print(f"{num}: Less than -10")
    elif num > -10: #greater than -10
      print(f"{num}: Greater than -10")
    else: #equal to -10
      print(f"{num}: Equal to -10")
  else: #odd
    print(f"{num}: Odd")
    num *= 2
    print(f"Updated Value: {num}")
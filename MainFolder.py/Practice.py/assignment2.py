
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
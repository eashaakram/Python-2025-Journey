#Practice
#Problem 1: Take a number, add 10, multiply by 2, then subtract 5 (use assignment operators).
#Take input
number = int(input("Enter any number: "))
#Addition
add = number + 10
#Multipliaction
multiply = add * 2
#Subtract
subtract = multiply - 5 
#Output
print("Result =",subtract)

#Problem 2: Take 3 numbers and check if first is greater than both second and third.
#Take input of 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
#Check
greater = a>b and a>c
#Output
print("Check if first is greater than both second and third:",greater)

#Problem 3: Take your name and age as input and print in format:
'''Hello Hamza,
You are 22 years old'''
#Take name & age as input
name = input("Enter your good name: ")
age = input("Enter your age: ")
#Output
print(f"Hello {name},\nYou are {age} years old")

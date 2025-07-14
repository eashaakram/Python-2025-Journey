#If else statement 
a = int(input("Enter your age:"))
print("Your age is",a)
if(a>18):
    print("You can drive") #indentation use in if-else to refer block of statement 
    print("Yes")           #basically indentation is a space before print
else:
    print("You can't drive")
    print("No")
print("Yay!")#this is not in block of statement
#Conditional Operators
# >,<,>=,<=,==,!=
print(a<18)
print(a>18)
print(a<=18)
print(a>=18)
print(a==18)
print(a!=18)

#example
apple = 120
budget = 200
if(apple <= budget):
    print("Alexa, add 1kg Apples to the cart")
else:
    print("Alexa, add 1kg Apples to the cart")

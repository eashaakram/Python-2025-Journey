def isEven(number1, number2):
    if(number1 % 2 == 0):
        print(number1,"is even")
    else:
        print(number1,"is odd")
    if(number2 % 2 == 0):
        print(number2,"is even")
    else:
        print(number2,"is odd")

number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
isEven(number1, number2)

# a, b = map(int, input("Enter two numbers separated by space: ").split())

# print("Product is:", a * b)

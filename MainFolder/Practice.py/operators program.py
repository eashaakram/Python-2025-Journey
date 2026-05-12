#Ask the user for two numbers and an operator (+, -, *, /).
#Use if-elif to perform the operation and show the result.

#Take inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
#Ask operator
op = input("Enter any operator(+,-,*,%,/,//): ")
#Check
if op == '+':
    print(f"{num1} {op} {num2} = {num1+num2} ")
elif op == '-':
    print(f"{num1} {op} {num2} = {num1-num2} ")
elif op == '*':
    print(f"{num1} {op} {num2} = {num1*num2} ")
elif op == '%':
    print(f"{num1} {op} {num2} = {num1%num2} ")
elif op == '/':
      if num2 != 0:
        print(f"{num1} {op} {num2} = {num1/num2} ")
      else:
        print("Error: Division by zero is not possible")
elif op == '//':
      if num2 != 0:
       print(f"{num1} {op} {num2} = {num1//num2} ")
      else:
        print("Error: Division by zero is not possible")
else:
     print("Invalid operator\nTry again...")    
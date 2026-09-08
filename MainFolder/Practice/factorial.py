# Factorial

number = int(input("Enter a number to find its factorial: "))

factorial = 1

if number == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial *= i
    # print(f"The factorial of {number} is {factorial}")
    print("The factorial of",number,"is",factorial)
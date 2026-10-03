# #Recursion Function
# #Factorial
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)

# print("\t===Factorial===")
# num = int(input("Enter any number:"))
# print("Factorial of",num,"is",factorial(num))

#Fibonacci Series
def fibonacci(n):
    if(n<0):
        print("Fibonacci numbers are only counted for positive numbers")
    elif(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print("\t===Fibonacci Series===")
num = int(input("Enter series number:"))
print("The series...")
# i = 0
# while(i<=num):
#     print(fibonacci(i),end=" ")
#     i+=1
# print(fibonacci(6))
for i in range(num+1):
    print(fibonacci(i),end=" ")
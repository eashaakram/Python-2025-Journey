#Take input
num = int(input("Enter any number: "))
if num <= 0:
    print("The number is neither composite nor prime")
elif num == 1:
    print("The number is composite")
else:
    for i in range(2,num):
        if num%i == 0:
            print("The number is composite")
            break #when it is divisible then stop it there 
    else: #if condition false then this for loop else part will run
        print("The number is prime")    
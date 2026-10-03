num = int(input("Enter a Number:"))
if(num < 0):
    print ("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is between 10-20")
    elif(num > 20 and num <= 30):
        print("Number is between 20-30")
    else:
        print("Number is greater than 30")
else:
    print("Number is zero")
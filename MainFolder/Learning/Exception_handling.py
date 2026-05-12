#Exception Handling
'''Syntax
try:
    statements which could generate error
except:
    Solution of generated exception'''
#These are codes that will handle errors and keep output running
#1
try:
    num = int(input("1)Enter an integer: "))#if u write Easha
except ValueError:
    print("Input entered is not an integer")#it will print when u enter wrong data 
print("Some code of lines")
print("End of program")

#2
try:
    num = int(input("2)Enter an integer: "))
    a = [6,3]#list
    print(a[num])
except ValueError:
    print("Input entered is not an integer")
except IndexError:
    print("Index Error")

#3
a = input("3)Enter the number: ")

try:
    print(f"Multiplication Table of {a} is:")
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
# except:
    # print("Invalid Input!")
except Exception as e:    
    print(e)
print("Some code of lines")
print("End of program")

#finally clause
def func1():
    try:
        l = [1,5,6,7]
        i = int(input("4)Enter the index:"))
        print(l[i])
        return 1
    except:
        print("Some erroe occured")
        return 0
    finally: #it is always executed
        print("I am always executed")


x = func1()
print(x)

#Now we are writing code that will generate error by programmer if user enter wrong input
#Raising custom error
a = int(input("5)Enter any value between 5 and 9: "))
if (a < 5 or a > 9):
    raise ValueError("Value should be between 5 and 9")

salary = int(input("Enter your salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

User = input("Enter The Value Between 5 And 9 : ")
try:
    if (User == "quit" or "Quit"):
        print("Better Luck Next Time!")
    else:
        if (int(User)>= 5 and int(User) <= 9):
            print(f"Congrulations! Your Entered Number {User} Is Between 5 And 9")
            print("Good Job!")
        elif (int(User) <= 4 or int(User) >= 10):
            raise ValueError("Error : Inavlid Input (Value Should Be In 5 And 9)")
except ValueError as e:
    print(e)

a = input("5)Enter any value between 5 and 9: ")
if a == "quit":
    print("The End")
elif (int(a) > 5 or int(a) < 9):
    print(f"The number {a} is between 5 and 9")   
elif (int(a) < 5 or int(a) > 9):
    raise ValueError("Value should be between 5 and 9")
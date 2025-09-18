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
print(f"Multiplication Table of {a} is:")
try:
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

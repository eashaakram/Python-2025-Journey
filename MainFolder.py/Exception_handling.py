#Exception Handling
'''Syntax
try:
    statements which could generate error
except:
    Solution of generated exception'''
#1
try:
    num = int(input("Enter an integer: "))#if u write Easha
except ValueError:
    print("Input entered is not an integer")#it will print when u enter wrong data 
print("Some code of lines")
print("End of program")

#2
try:
    num = int(input("Enter an integer: "))
    a = [6,3]#list
    print(a[num])
except ValueError:
    print("Input entered is not an integer")
except IndexError:
    print("Index Error")

#3
a = input("Enter the number: ")
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
#doc-strings
#doc-strings write just after or above the function defination
def square(n):
    '''Takes in a number n, returns the 
    square of n'''
    print(n**2)

square(5)
print(square.__doc__)
 
#if we don't write it after or above function defination then it will not doc-string
#like that
def square(n):
    print(n)
    '''Takes in a number n, returns the 
    square of n'''
    print(n**2)

square(5)
print(square.__doc__)#it will give none as output

#Zen of Python
import this
#Functions
#Built in functions start with def
def calculateGmean(a, b):  #function body
    mean = (a*b)/(a+b)
    print("Mean =",mean)
def isGreater(a , b):
    if (a>b):
        print("First number is greater")
    else:
        print("Second number is greater")
def islesser(a , b):
    pass #define it later so interpreter do not generate error

a = 2
b = 3
calculateGmean(a, b) #calling a function 
isGreater(a , b)





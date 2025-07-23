def average(a,b): #required argument here a and b       
    print("1)The average is",(a+b)/2)

average(4,6)

def averagee(c = 9, d = 1):  #default argument here give value to c and d
    print("2)The average is",(c+d)/2)

averagee() #we left it empty bcz above default argrument pass


def averageee(e = 9, f = 1):  #default argument here give value to c and d
    print("3)The average is",(e+f)/2)

averageee(1,5) #but if we write here values then default argument will get ignored


def avg(g = 9,h = 1):        
    print("4)The average is",(g+h)/2)
#keyword argument (order doesn't matter)
avg(h = 9,g = 21)
 
 
def ave(i,j = 1):        
    print("1)The average is",(i+j)/2)

ave(i = 21) #required argument, the value of i is complusory 
i = int(input("Enter any number:"))
while(i < 30):
    i = int(input("Enter any number:"))
    print(i)
print("Done with the loop")


i = int(input("Enter any number: "))
while(i < 30):
    print("i =",i)
    i += 1  # increment i to eventually break the loop
print("Done with the loop")

#Decrement Loop
count = 5
while(count > 0):
    print("Count =",count)
    count = count - 1 
    
 #else    
print("\nWith Else ")
t = -5
while(t > 0):
    print("t =",t)
    t = t - 1 
    #When while loop false it then print else part
else:
    print("I'm inside the else part")

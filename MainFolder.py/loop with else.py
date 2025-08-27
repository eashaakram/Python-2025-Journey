#for loop with else
for i in range(5):
    print(i)
else:
    print("Sorry no i")

#while loop with else
i = 0
while i<7:
    print(i)
    i=i+1
    if(i==4):
        print("Here the loop break")
        break
else:
    print("Sorry no i")

#format method
for x in range(5):
    print("Iteration number {} in for loop".format(x+1))
else:
    print("Else block i loop")
print("Out of loop")
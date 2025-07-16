name = "Python"
for i in name:
    print(i)
    # print(i, end=", ")
    if(i=="h"):
        print("there is something special")
for i in name:
    print(i, end=", ")
print("\n")

colors = ["Red", "Blue", "Green", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

#range
for k in range(5): #n-1
    print(k)
for k in range(5):
    print(k+1)
for k in range(1,11):
    print(k)
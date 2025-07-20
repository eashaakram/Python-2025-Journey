#Code of printing Table
number = int(input("Enter the number of which table you want:"))
for i in range(10):
    print(number,"*",i+1,"=",number*(i+1))
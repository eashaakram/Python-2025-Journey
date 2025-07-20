#Code of printing Table
number = int(input("Enter the number of which table you want:"))
print("===TABLE===")
for i in range(10):
    print(number,"*",i+1,"=",number*(i+1))
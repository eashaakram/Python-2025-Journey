# #Code of printing Table
# number = int(input("Enter the number of which table you want:"))
# for i in range(10):
#     print(number,"*",i+1,"=",number*(i+1))

while True:
    num = int(input("Enter a positive number:"))
    print(num)
    if not num > 0: #if num <= 0
        break
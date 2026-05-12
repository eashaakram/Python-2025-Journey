#Take input
num = int(input("Enter a number: "))
a = 0
b = 1
print("Fibonacci series:")
#print fibonacci series
for i in range(num):
  print(a,end=" ")
  temp = a
  a = b
  b = temp + b
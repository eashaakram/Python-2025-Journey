# #check the number is positive, negative and zero.

# while True:
#     i = str(input("Enter a number:"))
#     if i.lstrip('-').isdigit():
#       j = int(i)
#       while(j <= 0):
#        print("Invalid number\nEnter positive number again:")
#        j = int(input())
#       print(j,"is positive number")
#       break
#     else:
#        print("Invalid!Enter number like (1,2,3..)")

while True:
    i = str(input("Enter a number:"))
    if i.lstrip('-').isdigit():
      j = int(i)
      while(j <= 0):
       print("Invalid number\nEnter positive number again:")
       t = input()
       if t.lstrip('-').isdigit():
          j = int(t)
       else:
          print("Invalid!!Enter number like (1,2,3..)")
      print(j,"is positive number")
      break
    else:
       print("Invalid!Enter number like (1,2,3..)")

'''Problem 2: Take a number n from the user as input and display the even numbers from 1 to n. Use continue in while loop. 
Check if the number n is less then or equal to 1 display error.
'''
   #Take input
num = int(input("Enter a number: "))
#Check num < or = to 1
if num <= 1:
  print("Error: Number less or equal to 1\nEnter greater than 1")
else:
#display even number
  print("Even numbers are:")
  i = 1
  while (i <= num):
    if i % 2 != 0:
      i += 1
      continue
    else:
      print(i,end=" ")
      i += 1

'''Problem 3: Take a number n from the user as input and
 print the sum of even numbers and sum of odd numbers from 1 to n.
'''

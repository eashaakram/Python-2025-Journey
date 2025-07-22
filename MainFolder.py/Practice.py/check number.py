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
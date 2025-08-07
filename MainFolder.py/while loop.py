# # i = int(input("Enter any number:"))
# # while(i < 30):
# #     i = int(input("Enter any number:"))
# #     print(i)
# # print("Done with the loop")


# # i = int(input("Enter any number: "))
# # while(i < 30):
# #     print("i =",i)
# #     i += 1  # increment i to eventually break the loop
# # print("Done with the loop")

# # #Decrement Loop
# # count = 5
# # while(count > 0):
# #     print("Count =",count)
# #     count = count - 1 
    
# #  #else    
# # print("\nWith Else ")
# # t = -5
# # while(t > 0):
# #     print("t =",t)
# #     t = t - 1 
# #     #When while loop false it then print else part
# # else:
# #     print("I'm inside the else part")


# # count = 1
# # while (count <= 5):
# #     count += 1
# # print(count)

# # i = 1
# # while(i <= 100):
# #     print(i)
# #     i+=1
# # print("Another loop")
# # j = 100
# # while(j >= 1):
# #     print(j)
# #     j-=1

# # k = 1
# # while(k <= 100):
# #     print("Hi",k)
# #     k+=1

# # l = 1
# # print("L:-")
# # while(l <= 5):
# #    print(l)
# #    l+=1
# # print("Loop Ended")

# print("Table")
# n = int(input("Enter any number:"))
# i = 1
# while(i <= 10):
#     print(n,"*",i,"=",i*n)
#     i+=1

# # num = [1,4,9,11,25,36,49,64,81,100]
# # i = 0
# # while(i < len(num)):
# #     print(num[i])
# #     i += 1

# # heros = ["Ironman","Batman"]
# # i = 0
# # while(i < len(heros)):
# #     print(heros[i])
# #     i+=1
# # nums = (1,4,9,11,25,36,49,64,81,100,36)
# # x = 36
# # i = 0
# # while(i < len(nums)):
# #     if(nums[i] == x):
# #         print("FOUND at index",i)
# #     else:
# #         print("finding...")
# #     i+=1
    
# # a = 0
# # while a<3:
# #     if a==4:
# #         break
# #     print(a,end=", ")
# #     a+=1
# # else:
# #     print("\nLoop finished without break")

# i = 0
# a = "Akram"
# while(i < 10):
#     # print("Easha")
#     print(f"{i+1} times Easha {a}")
#     i+=1

# sum = 0
# i = 1
# while(i<=3):
#     sum+=i
#     i+=1
# print(f"Sum of the series is {sum}")    

# i = 9
# while(i>=0):
#     print(i)
#     i-=1

# #print series use while loop
# start = int (input("Enter starting number:"))
# stop = int (input("Enter ending number:"))
# if (start < stop ):
#     start+=1
#     while(start < stop):
#         print(start)
#         start+=1
#     else:
#         print("Invalid Inputs")

start = int (input("Enter starting number:"))
stop = int (input("Enter ending number:"))
while(stop <= start):
    print("Invalid number!\nStop number must be greater than start")
    start = int (input("Enter again starting number:"))
    stop = int (input("Enter again ending number:"))
while(start<stop):
    print(start)
    start+=1
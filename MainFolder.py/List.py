marks = [3, 5 , 6, "Eesha", True]
print(marks) #this will print whole list elements
print(marks[0]) #it will print 3 number at index zero
print(marks[1]) 
print(marks[2])
print(marks[3])
print(marks[4])

lst1 = [1, 2, 2, 3, 5, 4, 6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

details = ["Eesha", 19, "Akram", 9.8]
print(details)

#negative indexing
      #[0,1,2,3,4] positive index start from zero
mark = [3, 5, 6, "Python", False]
      #[-5,-4,-3,-2,-1] in negative 
print("Below there will four outputs of 6")
print(mark[-3])
print(mark[len(mark)-3]) #positive index
print(mark[5-3])
print(marks[2])

if 7 in mark:
    print("Yes, 7 in list mark")
else:
    print("No, 7 is not in list mark")
if 6 in mark:
    print("Yes, 6 in list mark")
else:
    print("No, 6 is not in list mark")
if "6" in mark:
    print("Yes, \'6\' in list mark")
else:
    print("No, \'6\' is not in list mark")
    #Some thing that applies for string
if "Py" in "Python":
    print("yes")

#List Comprehension
lst = [i for i in range(4)]
print (lst)
lst = [i*i for i in range(4)]
print (lst)
lst = [i*i for i in range(10)if i%2==0] #with condition
print (lst)

names = ["Mama","Papa","Brother","Sister"]
name = [item for item in names if "o" in item]
print(name)
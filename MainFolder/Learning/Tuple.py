# tup = (1,5,3)
# print(type(tup),tup)
# tup = (1) #it will print int type bcz we don't put coma at its end
# print(type(tup),tup)
# tup = (1,) #in tuple coma is necessay
# print(type(tup),tup)

# # tup = (1,2,16,343,98)
# # tup[0] = 90 
# # it will generate error because we can't change in tuple

# tup = [1,2,16,343,98] #it is list not tuple
# tup[0] = 90 
# print(tup)

# tup = (1,2,76)
# if 76 in tup:
#     print("Yes 76 is present")

# '''Tuples are imutable if you want to change tuple 
# then first convert it into list, make changes in it
# and then again convert back it into tuple'''

# countries = ("Spain", "Italy", "Pakistan", "England", "Germany")
# print("Countries before change:",countries)
# temp = list(countries)
# temp.append("Russia") #Add item
# temp.pop(3) #Remove item
# temp[2] = "Finland" #Change item
# countries = tuple(temp)
# print("Countries after change:",countries)

# country = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
# country2 = ("Vietnam", "India", "China")
# combine = country + country2
# print(combine)

# #Methods in Tuple
# tuple1 = (0,1,2,3,2,3,1,3,2,3)
# res = tuple1.count(3)
# print("3 comes in tuple1",res,"times")

# tuple1 = (0,1,2,3,2,3,1,3,2,3)
# res = tuple1.index(3)
# print("3 comes at index:",res)
# #slicing
# tuple1 = (0,1,2,3,2,3,1,3,2,3)
# res = tuple1.index(3,4,8)
# print("3 comes at index from index 4 to 7:",res)
# #length in tuple
# res = len(tuple1)
# print("Length of Tuple is",res)

# numbers = (2,3,1,4)
# print("Length :",len(numbers))
# sorted_num = sorted(numbers)
# print("Sorted numbers :",sorted_num)
# print("Sum of numbers :",sum(numbers))
# print("Minimum :",min(numbers))
# print("Maximum :",max(numbers))

##Mixed Data type tuple
data = ("Orange", 46, 3, 79, True, "Apple", "Apple", False)
#Display
print("Tuple data:", data)
#First and last element
print("First element is:",data[0])
print("Last element is:",data[-1])
#Count
item = "Apple"
print(f"{item} appears {data.count(item)} times")
#length
print("Length of tuple is:",len(data))
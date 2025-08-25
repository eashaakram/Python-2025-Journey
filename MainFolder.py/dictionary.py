# #dictionaries
# dic = {"Easha" : "Human being",
#        "Spoon" : "Object"}
# print(dic["Easha"])

# info = {"Name" : "Easha",
#         "Age" : 19,
#         "Eligible" : True}
# print(info) 

# #accessing keys
# print(info.keys()) 

# # accessing values
# print(info.values())

# # for key in info.keys(): 
# #     print(info[key])

# # for key in info.keys():
# #     print(f"The value of corresponding to key {key} is {info[key]}")

# for key,value in info.items():
#         print(f"The value of corresponding to key {key} is {value}")

# #Two ways of getting any single key
# print(info["Name"])#If I wrote Name2 it will generate error
# print(info.get("Name"))#If I wrote Name2 it will not generate error
# print(info.get("Name2"))#it will give output none

# print(info.items())
 

#Dictionary Methods
ep1={122:45, 78:82}
ep2={823:63, 72:27}
ep1.update(ep2)
ep1.clear() #it will print empty dictionary
print(ep1)

#create empty dictionary
empt = {}
print(empt)

ep3={122:45, 123:89, 67:69, 670:69}
#pop() is used to remove key
ep3.pop(122)
print(ep3)
#popitem() remove last item
ep4={122:45, 123:89, 67:69, 670:69}
ep4.popitem()
print (ep4)
ep5={122:45, 123:89, 67:69, 670:69}
del ep5
# print(ep5)generate error
ep6={122:45, 123:89, 67:69, 670:69}
del ep6[122]
print(ep6)

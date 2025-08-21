#dictionaries
dic = {"Easha" : "Human being",
       "Spoon" : "Object"}
print(dic["Easha"])

info = {"Name" : "Easha",
        "Age" : 19,
        "Eligible" : True}
print(info) 
#accessing keys
print("KEYS")
print(info.keys()) # -> 1 method
#accessing values
print("VALUES")
for key in info.keys(): # -> 2 method
    print(info[key])
print("end") 
#Two ways of getting any single key
print(info["Name"])#If I wrote Name2 it will generate error
print(info.get("Name"))#If I wrote Name2 it will not generate error
print(info.get("Name2"))#it will give output none
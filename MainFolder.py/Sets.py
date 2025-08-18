# #It is not set it will become dectionary 
# # harry = {}
# #for printing its type as a set we will write it like that
# harry = set()
# print(type(harry))

# info = {"Carla", 19, False, 5.9, 19} #Set will remove duplicates
# print(info)
# #Set is unordered
# for value in info:
#     print(value,end=" ")

# #Sets Methods
# s1 = {1,2,5,6}
# s2 = {3,6,4,7}
# print("Union =",s1.union(s2))
# s1.update(s2)
# print("Update =",s1,s2)

cities = {"Lahore", "Karachi", "Gujranwala", "Islamabad", "KPK"}
cities2 = {"Lahore", "Karachi", "KPK", "RWP"}
print("Union =",cities.union(cities2))
print("Intersection =",cities.intersection(cities2))
print("Intersection Update =",cities.intersection_update(cities2))
print("Symmetric Difference =",cities.symmetric_difference(cities2))
print("Disjoint =",cities.isdisjoint(cities2))
print("Superset =",cities.issuperset(cities2))
print("Subset =",cities.issubset(cities2))
print("Disjoint =",cities.isdisjoint(cities2))

cities.add("Easha")
print("Add =",cities)
cities.remove("Lahore")
print("Remove =",cities)
item = cities.pop()
print("Pop =",cities)
print("The element remove by pop =",item)


tup = (1,5,3)
print(type(tup),tup)
tup = (1) #it will print int type bcz we don't put coma at its end
print(type(tup),tup)
tup = (1,) #in tuple coma is necessay
print(type(tup),tup)

# tup = (1,2,16,343,98)
# tup[0] = 90 
# it will generate error because we can't change in tuple

tup = [1,2,16,343,98] #it is list not tuple
tup[0] = 90 
print(tup)

tup = (1,2,76)
if 76 in tup:
    print("Yes 76 is present")

'''Tuples are imutable if you want to change tuple 
then first convert it into list, make changes in it
and then again convert back it into tuple'''

countries = ("Spain", "Italy", "Pakistan", "England", "Germany")
print("Countries before change:",countries)
temp = list(countries)
temp.append("Russia") #Add item
temp.pop(3) #Remove item
temp[2] = "Finland" #Change item
countries = tuple(temp)
print("Countries after change:",countries)

country = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
country2 = ("Vietnam", "India", "China")
combine = country + country2
print(combine)
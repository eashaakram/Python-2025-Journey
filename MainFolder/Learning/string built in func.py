#String built in function 
a = "pYtHoN pRoGramInG"
print("Original:",a)
print("Upper Case:",a.upper())
print("Lower Case:",a.lower())
print("Capitalize:",a.capitalize()) #it will capitalize first character only
print("Title:",a.title()) #it will make capital first character of every word
print("Swap:",a.swapcase()) #it will change upper case into lower and lower into upper 

new = "python programming"
print("Find p at which index:",new.find("p")) #return index
print("Find k at which index if not then return -1 not error:",new.find("k"))
#control
print(new.find("p",3,15))
#              ,start,15-1

#reverse find
print("Reverse find p:",new.rfind("p"))
print("Reverse find n:",new.rfind("n,8,10")) #for error it will generate -1 not error directly


#Anything enclose in double or single quote is string
name = "Python"
print("This language is "+name)

#Another way to write it
print('Hello,"I am learning Python"')

#Triple single/double quote
print('''I'm Easha
 And I'm doing SE''')

#Accessing Character of string 
name = "Easha"
print(name[0]) #print first character of name Easha=E
print(name[1]) #print second character of name Easha=a
print(name[2]) #print second character of name Easha=s
print(name[3]) #print second character of name Easha=h
print(name[4]) #print second character of name Easha=a
#index 5 give an error

#for loop with string
for character in name:
 print(character)

#slicing in string
course = "Python,language"
print(len(course))
print("To start from zero index")
print(course[0:6]) 
print("To start from zero index without mention it")
print(course[:6]) #if we skip 0 Python atomatically consider zero 
print("To start from index 1")
print(course[1:6]) 
print("If we don't mention any index then it print full word")
print(course[:])

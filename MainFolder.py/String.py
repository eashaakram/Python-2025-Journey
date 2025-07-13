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
print(course[0:6]) #including zero but not 6
print("To start from zero index without mention it")
print(course[:6]) #if we skip 0 Python atomatically consider zero 
print("To start from index 1")
print(course[1:6]) 
print("If we don't mention any index then it print full word")
print(course[:])
print("If we mention negative in index then it will minus from total")
print(course[:-3])
print("One more way")
print(course[2:len(course)-3])
#Quick Quiz
nm = "harry"
print(nm[-4:-2])
print('''It will first minus 4 from total which is 5 so 
index start from 1 and then it will minus 2 from 5 which left with 
3 index so it will print from 1 to 3 index means 1,2 because in 
that form[1:3] 1 is included and 3 is excluded''')
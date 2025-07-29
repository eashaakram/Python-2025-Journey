l = [1,2,4,6]
print("L ",l)
l.append(7) #it will add 7 to original list
print("Append ",l)

l = [11,45,1,2,4,6]
print("L ",l)
l.sort()
print("Sort ",l)

l = [11,45,1,2,4,6]
l.sort(reverse = True)
print("Reverse Sort ",l)

l = [11,45,1,2,4,6]
l.reverse()
print("Reverse ",l)

l = [11,45,1,2,4,6]
m = l.copy()
m[0] = 0 #it will change value at index 0 but not in original list in copy list m
print("Copy ",l)
print("Copy ",m)

l = [11,45,1,2,4,6]
print("1 number is at index",l.index(1),"in list")

l = [11,45,1,2,4,6]
print("L ",l)
l.insert(1,899)
print("Insert value at index 1 ",l)


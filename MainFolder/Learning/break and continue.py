#break
for i in range(10):
    if (i == 5):
      break #it will stop here
    print("5 *",i+1,"=",5*(i+1))

#continue
for i in range(1,10):
    if (i == 5):
      print("skip")
      continue #it will just skip the iteration at 5
    print("2 *",i,"=",2*(i))

#do while loop
f = 0
while True:
   print(f)
   f+=1
   if(f%5==0):
    break
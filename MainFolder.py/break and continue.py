#break
for i in range(10):
    if (i == 5):
      break #it will stop here
    print("5 *",i+1,"=",5*(i+1))

#continue
for i in range(10):
    if (i == 5):
      print("skip")
      continue #it will just skip the iteration at 6
    print("2 *",i+1,"=",2*(i+1))

f = 0
while True:
   print(f)
   f+=1
   if(f%5==0):
    break
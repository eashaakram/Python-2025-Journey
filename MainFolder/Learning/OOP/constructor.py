class Employee:
    __name = None
    __id = 0
    __salary = 0
   
   #Constructor  
    def __init__(self,name,id,salary):
        self.__name = name
        self.__id = id
        self.__salary = salary
    def get_all(self):
         print('Name=',self.__name,end=", ")
         print('Id=',self.__id,end=", ")
         print('Salary=',self.__salary,end=" ")


    # def set_name(self,name): 
    #     self.__name = name 
    # def get_name(self): 
    #    return self.__name 
    

#main part
easha = Employee('Easha',420,7000000) 
easha.get_all()
# easha.set_name('Easha')
# print(easha.get_name())
class Employee:
    __name = None
    __id = 0
    __salary = 0
    #here double underscore means that variables are private
    def set_name(self,name): #self ka mtlb ha automatically object create hoga
        self.__name = name 
    def get_name(self): #self ka mtlb ha automatically object create hoga
       return self.__name 
    

#now creating object
easha = Employee() #here easha is object of class Employee
#print(easha.__name)  it give error because direct access not allow as this variable is private
easha.set_name('Easha')
print(easha.get_name())
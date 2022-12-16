class Demo():
    value=0
    def __init__(self,no1,no2):
        self.i=no1
        self.j=no2
    def fun(self):
        print("Inside fun")
        print(self.i,self.j)
    def gun(self):
        print("Inside gun")
        print(self.i,self.j)
value1=int(input("Enter No1:"))
value2=int(input("Enter No2:"))
#create object of demo class
Obj1=Demo(value1,value2)
Obj2=Demo(value1,value2)
#call the instance method
Obj1.fun()
Obj2.fun()
Obj1.gun()
Obj2.gun()


class Arithemetic:
    def __init__(self):
        self.value1=0
        self.value2=0
    def Accept(self,no1,no2):
        self.value1=no1
        self.value2=no2

    def Addition(self):
        return self.value1+self.value2

    def Subtraction(self):
        return self.value1-self.value2

    def Multiplication(self):
        return self.value1*self.value2

    def Division(self):
        return self.value1/self.value2

no1=int(input("Enter First No:"))
no2=int(input("Enter Second No:"))
obj=Arithemetic()
obj.Accept(no1,no2)

Add=obj.Addition()
print("Addition of No is:",Add)
Sub=obj.Subtraction()
print("Subtraction of No is:",Sub)
Mul=obj.Multiplication()
print("Multiplication of No:",Mul)
Div=obj.Division()
print("Division of No is:",Div)

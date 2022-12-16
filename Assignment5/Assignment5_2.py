class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0
    def Accept(self,radius):
        self.Radius=radius

    def CalculateArea(self):
        self.Area=self.PI*self.Radius*self.Radius
        return self.Area

    def CalculateCircumference(self):
        self.Circumference=2*Circle.PI*self.Radius
        return self.Circumference

    def Display(self):
        print("Radius:",self.Radius)
        Area=round(self.CalculateArea(),2)
        print("Area:",Area)
        Circumference=round(self.CalculateCircumference(),2)
        print("Circumference:",Circumference)
radius=int(input("Enter the Radius:"))
obj=Circle()
obj.Accept(radius)
obj.Display()





#Parent class
class Parent:
    def __init__(self,name,age):
        self.X= name
        self.t= age
    def printer(self):
        print(self.X,self.t)

x = Parent("Mzee",20)
x.printer()
#Child class
class Student(Parent):
 pass
y = Student("Kijana",30)
y.printer()
class shape:

    def __init__(self,H,W):
        self.H=H
        self.W=W
        print("I am in Super Class")
class triangle(shape):
    def area(self):
        self.Area=0.5*self.H*self.W

class rectangle(shape):
    def area(self):
        self.Area=self.H*self.W

t1=triangle(10,20)
r1=rectangle(10,20)

t1.area()
print(t1.Area)
r1.area()
print(r1.Area)
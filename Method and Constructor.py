class triangle:
    def __init__(self,height,width): #Constructor
     self.h=height
     self.w=width
     self.Area = 0.5 * self.h * self.w
    def area(self): #Method
        self.Area=0.5*self.h*self.w
    def display(self): #Method
        print(f"\nThe base = {self.w},\nThe Height = {self.h},\nThe area = {self.Area}")

t1=triangle(10,20)
t2=triangle(30,40)

t1.area()
t2.area()

t1.display()
t2.display()
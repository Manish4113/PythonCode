class shape:
    def __init__(self,x,y) :
        self.x=x
        self.y=y
    def area (self):
        return self.x*self.y  
class circle(shape):
    def __init__(self, r):
        self.r=r
        super().__init__(r,r)
    def area(self):
        return 3.14*self.r*self.r

a= shape(2,3)
print(a.area())    

b=circle(1)
print(b.area())
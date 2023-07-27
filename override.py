class math:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y   
class AllMath(math):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        super().__init__(x,y)
    def sub(self):
        return self.x-self.y   
    def multiply(self):
        return self.x*self.y
     


a=math(2,3)
print(a.add())
b=AllMath(58,1)
print(b.sub())
print(b.multiply())
    
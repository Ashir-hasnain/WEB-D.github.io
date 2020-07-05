class Circle:
    # pi = 3.14
    def __init__(self, radius, pi):
        self.radius= radius
        self.pi= pi
    def cur(self):
        return 2*self.pi*self.radius

c = Circle(4, 3.14) 
print(c)

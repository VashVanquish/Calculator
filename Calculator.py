import math

class Calculator():
    def __init__(self):
        self.A = 0
        self.B = 0
    def setA(self, num):
        self.A = num
    def setB(self, num):
        self.B = num
    def retA(self):
        return self.A
    def retB(self):
        return self.B
    def add(self):
        return self.A + self.B
    def sub(self):
        return self.A - self.B
    def mult(self):
        return self.A * self.B
    def div(self):
        return self.A / self.B
    def mod(self):
        return self.A % self.B
    def sqrt(self):
        return math.sqrt(self.A)
    def root(self):
        return self.A ** (1 / self.B)
    def expt(self):
        return self.A ** self.B
    def logm(self):
        return math.log(self.A, self.B)

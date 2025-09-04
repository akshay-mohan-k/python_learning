import math

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number * self.number
    
    def cube(self):
        return self.number * self.number * self.number
    
    def root(self):
        return math.sqrt(self.number)
    
    @staticmethod
    def greet():
        print("Hello")
    
num = Calculator(4)

num.greet()
print(num.square())
print(num.cube())
print(num.root())
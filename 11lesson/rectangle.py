"""class Rectangle():
    def  __init__(self,base,height):
        self.base = int(base) 
        self.height  = int(height)
    def area(self):
        return self.height * self.base
        
base = input("What is the base of your rectangle?:")
height = input ("What is the height of your rectangle?:")
rectangle = Rectangle(base,height)
area = rectangle.area()
print(area)"""

class Rectangle():
    def __init__(self,base,height):
        self.base=int(base)
        self.height = int(height)
        
    def area(self):
        return self.height * self.base
    def perimeter(self):
        return 2 * (self.height + self.base)
        
base = input("What is the base of your rectangle?:")
height = input ("What is the height of your rectangle?:")
rectangle = Rectangle(base,height)
print("The area of the rectangle is {} and its perimeter {}".format(rectangle.area(),rectangle.perimeter()))
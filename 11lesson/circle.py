import math
class Circle():
    def __init__(self,radius):
        self.radius=(radius)
       
        
    def area(self):
        return (radius **2) * math.pi
    def perimeter(self):
        return 2 * math.pi * (self.radius)
        

radius =int(input ("What is the radius of your circle?:"))

circle =Circle(radius)
print("The area of the circle is{} and its perimeter is{}".format(circle.area(), circle.perimeter()))


import math

def area_circle(radius):
    radius = int(radius)
    area = math.pi * radius * radius
    return area

user_radius = input("What is the radius of the circle?:")
calculated_area =  area_circle(user_radius)
print("The area of a circle with radius {} is {}".format(user_radius,calculated_area))
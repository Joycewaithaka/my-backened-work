def area_circle(radius):
    int_radius = int(radius)
    area = 22/7 * int_radius * int_radius
    return area
radius= input("What is your radius?:")
area = area_circle(radius)
print(area)
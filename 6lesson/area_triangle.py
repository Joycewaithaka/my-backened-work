def area_triangle(base,height):
    int_base = int(base)
    int_height = int(height)
    area = 0.5 * int_base * int_height
    return area
base = input("What is the base of your triangle?:")
height = input ("What is the height of your triangle?:")
area = area_triangle(base,height)
print(area)
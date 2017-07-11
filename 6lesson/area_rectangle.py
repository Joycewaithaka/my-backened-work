def area_rectangle(base,height):
    int_base = int(base)
    int_height = int(height)
    area = int_base * int_height
    return area
base = input("What is your base?:")
height = input("What is your height?:")
area = area_rectangle(base,height)
print(area)
    
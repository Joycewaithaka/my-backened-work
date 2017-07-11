import math
def sqrt (number):
    number = int(number)
    sqrt = math.sqrt(number)
    return sqrt
user_number = input("what is your number?:")
calculated_sqrt = sqrt(user_number)
print("The square root of {} is {}".format(user_number,calculated_sqrt))

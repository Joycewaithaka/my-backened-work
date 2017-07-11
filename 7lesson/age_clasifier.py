def age(age):
    age    = int(age)
    if  age <= 13:
        return ("Primary")
    elif age <=18:
        return ("Secondary")
    else:
       return ("Tertiary")
    
user_input = input("What is the students age?:")
computed_age = age(user_input)
print("The students group is {}".format(computed_age))
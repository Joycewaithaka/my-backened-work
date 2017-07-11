def grader(grade):
    grade = int(grade)
    if grade >= 90:
        return "A"
    elif grade >=70:
        return "B"
    elif grade >= 50:
        return "C"
    else:
        return "D"

user_input = input("What is the students marks?:")
computed_grade = grader(user_input)
print("The students grade is {}".format(computed_grade))
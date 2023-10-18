
math_marks = float(input("Enter math marks: "))
physics_marks = float(input("Enter physics marks: "))
geo_marks = float(input("Enter geography marks: "))
chem_marks = float(input("Enter chemistry marks: "))


if any(mark < 0 or mark > 100 for mark in [math_marks, physics_marks, geo_marks, chem_marks]):
    print("Unrecognized marks/average (Negative values or values greater than 100)")
else:

    average = (math_marks + physics_marks + geo_marks + chem_marks) / 4


    if average >= 71 and average <= 100:
        print("Grade: A")
    elif average >= 51:
        print("Grade: B")
    elif average >= 31:
        print("Grade: C")
    else:
        print("Grade: D")
number = int(input('Enter number: '))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Get marks for four subjects: math, physics, geography, and chemistry
math_marks = float(input("Enter math marks: "))
physics_marks = float(input("Enter physics marks: "))
geo_marks = float(input("Enter geography marks: "))
chem_marks = float(input("Enter chemistry marks: "))

# Check for negative values or values greater than 100
if any(mark < 0 or mark > 100 for mark in [math_marks, physics_marks, geo_marks, chem_marks]):
    print("Unrecognized marks/average (Negative values or values greater than 100)")
else:
    # Calculate the average
    average = (math_marks + physics_marks + geo_marks + chem_marks) / 4

    # Assign a grade based on the average
    if average >= 71 and average <= 100:
        print("Grade: A")
    elif average >= 51:
        print("Grade: B")
    elif average >= 31:
        print("Grade: C")
    else:
        print("Grade: D")






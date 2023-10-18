# 1. Write a program that checks whether a number is zero, positive or negative
# 2. Grading system: - DONE
#       A: 71 - 100
#       B: 51 - 70
#       C: 31 - 50
#       D: 0 - 30
# 3. No negative values - DONE
# 4. No values greater than 100 - DONE
# 5. Get average of Maths, Physics, Geo and Chem - DONE
# 6. Grades are displayed depending on average - DONE
# 7. The program displays 'Unrecognized marks/avg' if value is negative - DONE
# 8. The program displays 'Unrecognized marks/avg' if value is greater than 100 - DONE

# Greet the user:
#   a. Enter Math grades
#       i. If math grades meet the criteria, move to the next section
#           ->Enter Physics grades
#               & If physics grades meet the criteria, move to the next section
#                   + Enter Geo grades
#                       % If geo grades meet the criteria, move to the next section
#                           ^ Enter Chem grades
#                           ^ If not, display error message
#                              -> Check If number is negative
#                              -> Check if number is greater than 100
#                       %If not, display error message
#                          -> Check If number is negative
#                          -> Check if number is greater than 100
#               & If not, display error message
#                    -> Check If number is negative
#                    -> Check if number is greater than 100
#         ii. If not, display error message
#           -> Check If number is negative
#           -> Check if number is greater than 100

# Greet the user:

print("Hello, Welcome to The Grading System :-).")
print("Kindly Enter Your Marks as indicated:")

# Collecting the scores while checking if the score is valid or not.

while True:
    try:
        math = float(input('Please Key in your Mathematics Marks: '))
        if 0 <= math <= 100:
            print("Your Mathematics score is: ")
            print(math)
            if math ==0:
                print("This is zero")
            else:
                print("It is a positive value")
            while True:
                try:
                    phy = float(input('Please Key in your Physics Marks: '))
                    if 0 <= phy <= 100:
                        print("Your Physics score is: ")
                        print(phy)
                        if phy == 0:
                            print("This is zero")
                        else:
                            print("It is a positive value")
                        while True:
                            try:
                                geo = float(input('Please Key in your Geography Marks: '))
                                if 0 <= geo <= 100:
                                    print("Your Geography score is: ")
                                    print(geo)
                                    if geo == 0:
                                        print("This is zero")
                                    else:
                                        print("It is a positive value")
                                    while True:
                                        try:
                                            chem = float(input('Please Key in your Chemistry Marks: '))
                                            if 0 <= chem <= 100:
                                                print("Your Physics score is: ")
                                                print(chem)
                                                if chem == 0:
                                                    print("This is zero")
                                                else:
                                                    print("It is a positive value")
                                                break

                                            elif chem > 100:
                                                print(chem)
                                                print("It is a positive value")
                                                print("You have keyed in unrecognized marks/avg")
                                                print("Please Enter Valid Marks")

                                            else:
                                                print(chem)
                                                print("It is a negative value")
                                                print("You have keyed in unrecognized marks/avg")
                                                print("Please Enter Valid Marks")

                                        except ValueError:
                                            print("Invalid input. Please enter a numerical value.")

                                    break

                                elif geo > 100:
                                    print(geo)
                                    print("It is a positive value")
                                    print("You have keyed in unrecognized marks/avg")
                                    print("Please Enter Valid Marks")

                                else:
                                    print(geo)
                                    print("It is a negative value")
                                    print("You have keyed in unrecognized marks/avg")
                                    print("Please Enter Valid Marks")

                            except ValueError:
                                print("Invalid input. Please enter a numerical value.")

                        break

                    elif phy > 100:
                        print(phy)
                        print("It is a positive value")
                        print("You have keyed in unrecognized marks/avg")
                        print("Please Enter Valid Marks")

                    else:
                        print(phy)
                        print("It is a negative value")
                        print("You have keyed in unrecognized marks/avg")
                        print("Please Enter Valid Marks")

                except ValueError:
                    print("Invalid input. Please enter a numerical value.")

            break

        elif math > 100:
            print(math)
            print("It is a positive value")
            print("You have keyed in unrecognized marks/avg")
            print("Please Enter Valid Marks")


        else:
            print(math)
            print("It is a negative value")
            print("You have keyed in unrecognized marks/avg")
            print("Please Enter Valid Marks")

    except ValueError:
        print("Invalid input. Please enter a numerical value.")

# Total Score

sum = math + phy + geo + chem

print("This is your total score: ")
print(sum)

# Average score

avg = sum/4

print("This is your average score: ")
print(avg)

# Final grade

print("This is your Final Grade: ")

if avg >= 71 and avg <= 100:
    print("A")

elif avg >= 51 and avg <= 70:
    print("B")

elif avg >= 31 and avg <= 50:
    print("C")

elif avg >= 0 and avg <= 30:
    print("D")

print("Thank you for using the Grading System!!!")







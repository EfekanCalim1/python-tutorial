print("Welcome to Grade Calculator")
maths_grade = int(input("What is your maths grade? " ))
chemistry_grade = int(input("What is your chemistry grade? "))
physics_grade = int(input("What is your physics grade? "))

average = (maths_grade + chemistry_grade + physics_grade)/3

print("Your average grade is", average)

if average >= 70:
    overall = "A"
    print("Your overall grade is", overall)
elif average >= 60:
    overall = "B"
    print("Your overall grade is", overall)
elif average >= 50:
    overall = "C"
    print("Your overall grade is", overall)
elif average >= 40:
    print("Your overall grade is", overall)
elif average < 40:
    print("Fail")


                  

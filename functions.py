name = input("Enter your name: ")
homework = int(input("Enter your homework score: "))
assessment = int(input("Enter your assessment score: "))
final_exam= int(input("Enter your final exam grade: "))

def grade_calculator(homework, assessment, final_exam):
    if homework > 25 or assessment > 50 or final_exam > 100:
        return "Invalid scores entered"
    total = homework + assessment + final_exam
    grade = (total / 175) * 100
    return grade

def grade_boundaries(percent_score):
    final_letter_grade = ""
    if percent_score > 80:
        final_letter_grade = "A"
    elif percent_score > 70:
        final_letter_grade = "B"
    elif percent_score > 60: 
        final_letter_grade = "C"
    elif percent_score > 50:
        final_letter_grade = "D"
    else:
        final_letter_grade = "F"
    return final_letter_grade
    
grade = grade_calculator(homework, assessment, final_exam)

letter_grade = grade_boundaries(grade)

print(f"{name} got {grade}%, final grade {letter_grade}")

 

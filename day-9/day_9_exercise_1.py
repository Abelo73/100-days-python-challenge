# Day 9.1 Grading Exercise



student_scores = {
    "Harry":81,
    "Ron":78,
    "Hermine":99,
    "Draco":74,
    "Neville":62,
}


student_grades = {}

for student in student_scores:
    score = student_scores[student]
    # print(score)
    if score >90:
        student_grades[student] = "Outstanding"
    elif score >80:
        student_grades[student] = "Exactly Expected"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# above 91 | outstanding
# above 81 | Exactly Expected
# above 71 | Acceptable
# 70 or lower | Fail



print(student_grades)
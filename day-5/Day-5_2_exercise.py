# 5.2 Highest Score Exercise

    

# student_score = [78, 65, 89, 55, 91, 64, 89]
student_scores = (input("Input a list of student scores: \n").split()
)
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score is {highest_score}")
# wwite your solution here
def student_information():
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")

    names = {}
    with open(student_info) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            stud_info = line.split(";")
            if stud_info[0] == "id":
                continue
            names[stud_info[0]] = stud_info[1] + " " + stud_info[2]
    
    ex_data = {}
    with open(exercise_data) as data_file:
        for line in data_file:
            line = line.replace("\n", "")
            stud_data = line.split(";")
            if stud_data[0] == "id":
                continue
            ex_data[stud_data[0]] = []
            for grades in stud_data[1:]:
                ex_data[stud_data[0]].append(int(grades))
    
    exam_data = {}
    with open(exam_points) as exam_file:
        for line in exam_file:
            line = line.strip()
            exam_scores = line.split(";")
            if exam_scores[0] == "id":
                continue
            sum = 0
            for scores in exam_scores[1:]:
                sum += int(scores)
            exam_data[exam_scores[0]] = sum

    for key, value in names.items():
        if key in ex_data and key in exam_data:
            name = value
            courses = ex_data[key]
            sum = 0
            for course in courses:
                sum += int(course)
            exam_marks = exam_data[key]
            total_scores = (sum//4) + exam_marks
            grade = get_grade(total_scores)
            print(f"{name} {grade}")

def get_grade(score:int):
    if score < 15:
        return 0
    if score < 18:
        return 1
    if score < 21:
        return 2
    if score < 24:
        return 3
    if score < 28:
        return 4
    return 5


def main():
    student_information()


main()



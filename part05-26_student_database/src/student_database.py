# Write your solution here
def add_student(student_list: dict, name:str):
    if name not in student_list:
        student_list[name] = []
    
def print_student(student_list:dict, name:str):
    if name not in student_list:
        print(f"{name}: no such person in the database")
    else:
        print(f"{name}: ")
        if len(student_list[name]) == 0:
            print(" no completed courses")
        else:
            print(f" {len(student_list[name])} completed courses:")
            sum = 0
            for course_info in student_list[name]:
                print(f"  {course_info[0]} {course_info[1]}")
                sum += course_info[1]
            average = float(sum/len(student_list[name]))
            print(f" average grade {average}")

def add_course(student_list: dict, name:str, course_info:tuple):
    if name in student_list and course_info[1] > 0:
        if len(student_list[name]) == 0:
            student_list[name].append(course_info)
        else:
            course_list = []
            for course in student_list[name]:
                course_list.append(course[0])
            if course_info[0] not in course_list:
                student_list[name].append(course_info)
            else:
                key_list = [x[0] for x in student_list[name]]
                location = key_list.index(course_info[0])
                if course_info[1] > student_list[name][location][1]:
                    student_list[name][location] = course_info
                

def summary(student_list:dict):
    print(f"students {len(student_list)}")
    
    most_courses = 0
    person = ""

    ave = 0.0
    average_person = ""

    for student in student_list:
        if len(student_list[student]) > most_courses:
            person = student
            most_courses = len(student_list[student])
        sum = 0
        for course_info in student_list[student]:
            sum+= course_info[1]
            average = float(sum/len(student_list[student]))
            if average > ave:
                ave = average
                average_person = student
    
    print(f"most courses completed {most_courses} {person}")
    print(f"best average grade {ave} {average_person}")



if __name__ == "__main__":
    students = {}

    add_student(students, "shegs")
    add_student(students, "kule")
    print_student(students, "shegs")
    print_student(students, "kule")
    print_student(students, "amakiri-jack")
    add_course(students, "kule", ("fine girl 101", 3) )
    add_course(students, "kule", ("fine girl 103", 3) )
    add_course(students, "kule", ("fine girl 101", 4) )
    print_student(students, "kule")
    summary(students)



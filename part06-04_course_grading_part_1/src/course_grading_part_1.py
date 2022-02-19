# write your solution here
def student_information():
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")

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

    for key, value in names.items():
        if key in ex_data:
            name = value
            courses = ex_data[key]
            print (f"{name} {sum(courses)}")



def main():
    student_information()


main()


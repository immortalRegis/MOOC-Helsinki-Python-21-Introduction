# tee ratkaisu tänne
# tee ratkaisu tänne
def student_information():
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
    course_info = input("Course information: ")

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

    nam = "name"
    exec_nb = "exec_nbr"
    exec_pt = "exec_pts."
    exm_pt = "exm_pts."
    tot_pt = "tot_pts."
    grd = "grade"  

    course_name = ""
    study_credits = ""
    with open(course_info) as info_file:
        for row in info_file:
            if "name" in row:
                row = row.split(":")
                course_name = row[1].strip()
            if "study credits" in row:
                row = row.split(":")
                study_credits = row[1].strip()

    with open("results.txt", "w") as result_file, open("results.csv","w") as summary:
        header = (f"{course_name}, {study_credits} credits" +"\n")
        result_file.write(header)
        result_file.write("="*(len(header)-1) + "\n")
        result_file.write(f"{nam:30}{exec_nb:10}{exec_pt:10}{exm_pt:10}{tot_pt:10}{grd:10}" +"\n")
    
        for key, value in names.items():
            if key in ex_data and key in exam_data:
                name = value
                courses = ex_data[key]
                exec_nbr = 0
                
                for course in courses:
                    exec_nbr += int(course)
                exec_pts = exec_nbr//4
                
                exm_pts = exam_data[key]
                tot_pts = exec_pts + exm_pts
                grade = get_grade(tot_pts)
                
                exc = str(exec_nbr)
                exp = str(exec_pts)
                xmp = str(exm_pts)
                tp = str(tot_pts)
                gr = str(grade)

                single_entry = (f"{name:30}{exc:10}{exp:10}{xmp:10}{tp:10}{gr:10}")
                result_file.write(single_entry + "\n")
                summary_entry = f"{key};{value};{gr}"
                summary.write(summary_entry + "\n")
        
        
    print("Results written to files results.txt and results.csv")            

def get_grade(score:int):
    a = 0
    limits = [15,18, 21, 24, 28]
    while a < 5 and score >= limits[a]:
        a += 1
    return a


def main():
    student_information()


main()
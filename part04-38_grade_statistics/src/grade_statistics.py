# Write your solution here
def main():
    exam_points = []
    exercise_points = []

    while True:
        value = input("Exam points and exercises completed: ")
        if len(value) == 0:
            break
        sep_value = value.split()
        exam_points.append(sep_value[0])
        exercise_points.append(sep_value[1])


    print("Statistics:")
    average_points = points_average(exam_points, exercise_points)
    print(f"Points average: {average_points:.1f}")

    passed_percentage = percentage_passed(exam_points, exercise_points)
    print(f"Pass percentage: {passed_percentage:.1f}")
    
    grade_distribution(exam_points, exercise_points)

def points_average(exam_list: list, exercise_list: list):
    sum = 0
    exam_score = [int(i) for i in exam_list]
    exercise_score = [int(j) for j in exercise_list]

    for i in range(len(exam_list)):
        sum += exam_score[i] + (exercise_score[i]//10)

    return float(sum/len(exam_list))


def percentage_passed(exam_list: list, exercise_list: list):
    fail = 0
    exam_score = [int(i) for i in exam_list]
    exercise_score = [int(j) for j in exercise_list]

    for i in range(len(exam_list)):
        total_score = exam_score[i] + (exercise_score[i]//10) 
        if ( total_score < 15) or (exam_score[i] < 10):
            fail += 1

    return float (100*(len(exam_list) - fail)/len(exam_list))

def grade_distribution(exam_list: list, exercise_list: list):
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    exam_score = [int(i) for i in exam_list]
    exercise_score = [int(j) for j in exercise_list]

    for i in range(len(exam_list)):
        total_score = exam_score[i] + (exercise_score[i]//10)
        if ( total_score < 15) or (exam_score[i] < 10):
            zero += 1
        elif total_score < 18:
            one += 1
        elif total_score < 21:
            two += 1
        elif total_score < 24:
            three += 1
        elif total_score < 27:
            four += 1
        else:
            five += 1
    
    print("Grade distribution:")
    print("5:", five*"*" )
    print("4:", four*"*" )
    print("3:", three*"*" )
    print("2:", two*"*" )
    print("1:", one*"*" )
    print("0:", zero*"*" )


main()
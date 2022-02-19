# write your solution here
def matrix_sum():
    numbers = get_numbers_in_list()
    
    sum = 0
    for number in numbers:
        sum += number
    return sum

def matrix_max():
    numbers = get_numbers_in_list()
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

def row_sums():
    sum_list = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n","")
            row = line.split(",")
            sum = 0
            for element in row:
                sum += int(element)
            sum_list.append(sum)
    return sum_list
   
def get_numbers_in_list():
    numbers_list = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            for number in numbers: 
                numbers_list.append(int(number))
    return numbers_list

if __name__ == "__main__":
    row_sums()
# write your solution here
def largest():
    largest_number = 0
    with open("numbers.txt") as new_file:
        for line in new_file:
            pure_line = line.replace("\n", "")
            line_value = int(pure_line)
            if line_value > largest_number:
                largest_number = line_value
    return largest_number


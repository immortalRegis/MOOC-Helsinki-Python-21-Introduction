# Write your solution here
def filter_solutions():
    correct_list = []
    incorrect_list = []
    with open("solutions.csv") as new_file:    
        for row in new_file:
            sep_row = row.strip()
            sep_row_list = sep_row.split(";")
            contents = split_string(sep_row_list[1])
            
            number1 = contents[0]
            number2 =  contents[1]
            operation = contents[2]

            if operation == "+":
                if str(number1 + number2) == sep_row_list[2]:
                    correct_list.append(sep_row + "\n")
                else:
                    incorrect_list.append(sep_row + "\n")
            else:
                if str(number1 - number2) == sep_row_list[2]:
                    correct_list.append(sep_row + "\n")
                else:
                    incorrect_list.append(sep_row + "\n") 
        with open("correct.csv", "w") as new_file:
            for record in correct_list:
                new_file.write(record)
        with open("incorrect.csv", "w") as new_file:
            for record in incorrect_list:
                new_file.write(record)  




def split_string(calc:str):
    operand_index = calc.find("-")
    if operand_index == -1:
        operand_index = calc.find("+")
    
    n1 = int(calc[0:operand_index])
    n2 = int(calc[operand_index+1:])

    return (n1, n2, calc[operand_index])
    
if __name__ == "__main__":
    filter_solutions()


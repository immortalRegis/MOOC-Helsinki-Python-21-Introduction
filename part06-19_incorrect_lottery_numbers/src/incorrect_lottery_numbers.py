# Write your solution here
def filter_incorrect():
    with open("lottery_numbers.csv") as new_file, open ("correct_numbers.csv","w") as correct_file:
        for line in new_file:
            line = line.strip()
            records = line.split(";")
            str_wk_nmbr = records[0].split(" ")
            try:
                wk_num = int(str_wk_nmbr[1])
            except:
                continue
            numbers = records[1].split(",")
            if len(numbers) < 7:
                #raise ValueError("Data corrupted")
                continue
            wrong_number = False
            for i in range(len(numbers)):
                try:
                    num_value = int(numbers[i])
                except ValueError:
                    wrong_number = True
                    break
            if wrong_number:
                continue
            empty_number_holder = []
            for i in range(len(numbers)):
                num_value = int(numbers[i])
                if num_value < 1 or num_value > 39:
                    wrong_number = True
                    break
                if num_value in empty_number_holder:
                    wrong_number = True
                    break
                empty_number_holder.append(num_value)
            if wrong_number:
                continue 
            correct_file.write(line + "\n")

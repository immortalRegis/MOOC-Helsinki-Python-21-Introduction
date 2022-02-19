# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False
    
    day = int(pic[0:2])
    month = int(pic[2:4])
    year = int(pic[4:6])

    century_marker = pic[6]
    if not century_marker in ["A", "+", "-"]:
        return False
    if century_marker == "A":
        year += 2000
    elif century_marker == "+":
        year += 1800
    else:
        year += 1900

    try:
        correct_date = datetime(year, month, day)
    except ValueError:
        return False

    control_character = int(pic[0:6] + pic[7:10])
    index = control_character % 31
    
    character_set = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    if pic[10] != character_set[index]:
        return False

    return True

if __name__ == "__main__":
    print(is_it_valid("230827-906F"))

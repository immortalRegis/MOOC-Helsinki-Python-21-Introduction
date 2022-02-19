# Write your solution here
from string import ascii_lowercase
import random

def generate_strong_password(length: int, add_num: bool, spec_char: bool):
    super_set = ascii_lowercase
    password = random.choice(super_set)
    numbers = "0123456789"
    special_characters = "!?=+-()#"

    if add_num:
        password += random.choice(numbers)
        super_set = ascii_lowercase + numbers
    if spec_char:
        password += random.choice(special_characters)
        super_set = ascii_lowercase + special_characters
     
    while len(password) < length:
        password += random.choice(super_set)
    
    return password

if __name__ == "__main__":
   print(generate_strong_password(5, False, True))




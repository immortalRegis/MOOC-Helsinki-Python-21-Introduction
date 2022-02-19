# Write your solution here
import string
def separate_characters(my_string: str):
    letters = ""
    special_chars = ""
    others = ""

    for char in my_string:
        if char in string.ascii_letters:
            letters += char
        elif char in string.punctuation:
            special_chars += char
        else:
            others += char
    
    return (letters, special_chars, others)
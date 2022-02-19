# Write your solution here
from string import ascii_letters

def change_case(orig_string: str):
    new_string = ""
    for letter in orig_string:
        if letter == (letter.upper()):
            letter = letter.lower()
        else:
            letter = letter.upper()
        new_string += letter
    return new_string

def split_in_half(orig_string: str):
    string_length = len(orig_string)
    midpoint = string_length // 2
    return (orig_string[0:midpoint], orig_string[midpoint:])

def remove_special_characters(orig_string: str):
    new_word = ""
    for character in orig_string:
        if character == " " or character.isdigit() or character in ascii_letters:
            new_word += character
    return new_word

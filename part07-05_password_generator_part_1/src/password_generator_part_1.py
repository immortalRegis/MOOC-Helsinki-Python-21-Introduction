# Write your solution here
from string import ascii_lowercase
from random import sample

def generate_password(length: int):
    characters = list(ascii_lowercase)
    random_characters = sample(characters, length)
    
    password = ""
    for letter in random_characters:
        password += letter
    
    return password


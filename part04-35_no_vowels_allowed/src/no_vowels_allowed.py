# Write your solution here
def no_vowels(phrase: str):
    new_phrase = ""
    for character in phrase:
        if character not in "aeiou":
            new_phrase += character
    return new_phrase 
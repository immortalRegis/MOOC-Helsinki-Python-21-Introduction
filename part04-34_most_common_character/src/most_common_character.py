# Write your solution here
def most_common_character(word: str):
    letter_count = 0
    common_character = word[0]
    
    for letter in word:
        if word.count(letter) > word.count(common_character):
            common_character = letter
    return common_character

# Write your solution here
def histogram(word: str):
    my_dictionary = {}

    for letter in word:
        if letter not in my_dictionary:
            my_dictionary[letter] = 0
        my_dictionary[letter] += 1
    
    for key, value in my_dictionary.items():
        print(f"{key} ", end="")
        print(value * "*")
# Write your solution here
def all_the_longest(holder: list):
    longest_length = 0
    for word in holder:
        if len(word) > longest_length:
            longest_length = len(word)
    
    longest_list = []
    for word in holder:
        if len(word) == longest_length:
            longest_list.append(word)
    return longest_list
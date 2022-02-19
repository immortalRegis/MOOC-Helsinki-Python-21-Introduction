# Write your solution here
def length_of_longest (holder: list):
    longest = 0
    for word in holder:
        if len(word) > longest:
            longest = len(word)
    
    return longest
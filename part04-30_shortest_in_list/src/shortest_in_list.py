# Write your solution here
def shortest(holder: list):
    shortest = holder[0]
    
    for word in holder:
        if len(word) < len(shortest):
            shortest = word
    return shortest
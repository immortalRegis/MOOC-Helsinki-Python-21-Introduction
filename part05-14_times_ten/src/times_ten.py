# Write your solution here
def times_ten(start_index: int, end_index: int):
    my_dictionary = {}
    i = start_index

    while i <= end_index:
        my_dictionary[i] = (10*i)
        i += 1
    
    return my_dictionary
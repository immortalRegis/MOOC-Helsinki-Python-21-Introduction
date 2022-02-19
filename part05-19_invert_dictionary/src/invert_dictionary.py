# Write your solution here
def invert(my_dictionary: dict):
    temp_dict = {}

    for key, value in my_dictionary.items():
        temp_dict[value] = key
    
    my_dictionary.clear()
    my_dictionary.update(temp_dict)
 

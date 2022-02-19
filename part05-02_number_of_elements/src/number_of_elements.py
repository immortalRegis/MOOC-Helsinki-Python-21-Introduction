# Write your solution here
def count_matching_elements(my_list: list, element: int):
    count = 0

    for row in my_list:
        for num in row:
            if num == element:
                count += 1
    
    return count
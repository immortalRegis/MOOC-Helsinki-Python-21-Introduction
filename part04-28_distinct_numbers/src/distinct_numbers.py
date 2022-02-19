# Write your solution here
def distinct_numbers(my_list: list):
    new_list = []
    sorted_list = sorted(my_list)

    for num in sorted_list:
        if num in new_list:
            continue
        new_list.append(num)
    return new_list
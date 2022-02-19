# Write your solution here
def list_sum(first_list: list, second_list: list):
    new_list = []
    for i in range(0, len(first_list)):
        sum = first_list[i] + second_list[i]
        new_list.append(sum)
    return new_list
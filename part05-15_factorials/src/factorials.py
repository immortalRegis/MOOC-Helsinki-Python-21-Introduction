# Write your solution here
def factorials(n: int):
    my_dictionary = {}

    for i in range(1, n + 1):
        my_dictionary[i] = get_factorial(i)

    return my_dictionary

def get_factorial(num: int):
    if num == 1 or num == 0:
        return 1
    return num * get_factorial(num - 1)
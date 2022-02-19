# Write your solution here
def formatted(holder: list):
    new_list = []
    for num in holder:
        value = f"{num:.2f}"
        new_list.append(value)
    return new_list
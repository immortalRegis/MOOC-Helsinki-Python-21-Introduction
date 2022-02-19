# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        fruit_dict = {}

        for line in new_file:
            line = line.replace("\n","")
            parts = line.split(";")
            fruit_dict[parts[0]] = float(parts[1])
    return fruit_dict
        
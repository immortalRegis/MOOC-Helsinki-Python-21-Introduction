# Write your solution here
def everything_reversed(my_list: list):
    received_list = []
    for item in my_list:
        received_list.append(item[::-1])
    
    new_list = received_list[::-1]
    return new_list

if __name__ == "__main__":
    everything_reversed(["abc", "def"])
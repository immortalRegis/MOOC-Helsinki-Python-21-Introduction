# Write your solution here
def mean(given_list : list):
    if len(given_list) > 0:
        return sum(given_list) / len(given_list)
    return 0
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
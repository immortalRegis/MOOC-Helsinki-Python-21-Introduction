# Write your solution here
def longest_series_of_neighbours(my_list: list):
    largest_chain_length = 0
    current_chain_length = 0

    for i in range(len(my_list) - 1):
        if abs(my_list[i + 1] - my_list[i]) == 1:
            current_chain_length += 1
            if current_chain_length > largest_chain_length:
                largest_chain_length = current_chain_length
        else:
            current_chain_length = 0         
    return largest_chain_length + 1

if __name__ == "__main__":
    print(longest_series_of_neighbours([1, 2, 3, 5, 6, 9, 10]))
# Write your solution here
def list_of_stars(given_list: list):
    for number in given_list:
        print(number * "*")


if __name__ == "__main__":
    list_of_stars([2,3,4])

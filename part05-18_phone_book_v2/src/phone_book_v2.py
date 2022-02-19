# Write your solution here
def search(given_dictionary: dict):
    name = input("name: ")
    if name in given_dictionary:
        for number in given_dictionary[name]:
            print(number)
    else:
        print("no number")

def add(given_dictionary: dict):
    name = input("name: ")
    number = input("number: ")

    if not name in given_dictionary:
        given_dictionary[name] = []
    
    given_dictionary[name].append(number)
    print("ok!")
    

def main():
    my_dictionary = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit):"))
        if command == 1:
            search(my_dictionary)
        if command == 2:
            add(my_dictionary)
        if command == 3:
            break
    print("quitting...")

main()
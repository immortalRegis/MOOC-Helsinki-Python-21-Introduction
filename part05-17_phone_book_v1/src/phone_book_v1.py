# Write your solution here
def phone_book(my_dictionary: dict):
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 3:
            break
        elif command == 1:
            name = input("name: ")
            if name in my_dictionary:
                print(my_dictionary[name])
            else:
                print("no number")
        elif command == 2:
            name = input("name: ")
            number = input("number: ")
            my_dictionary[name] = number
            print("ok!")

    print("quitting...")
        

def main():
    my_dictionary = {}

    my_dictionary["john"] = "23456090000"
    my_dictionary["jane"] = "23788948930"
    phone_book(my_dictionary)

main()
# Write your solution here
def read_input(message:str, n1:int, n2:int):
    while True:
        try:
            inpt_str = input(message)
            number = int(inpt_str)
            if number >= n1 and number <=n2:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {n1} and {n2}")

if __name__ == "__main__":
    number = read_input("Enter value: ", 5, 10)
    print(f"{number} is the number")
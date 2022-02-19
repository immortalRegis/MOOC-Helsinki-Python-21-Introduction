# Write your solution here
def line(length, characters):
    if len(characters) == 0:
        print(length * "*")
    else:
        print(length * characters[0])
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
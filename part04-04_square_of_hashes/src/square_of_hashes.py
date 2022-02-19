# Copy here code of line function from previous exercise
def line(length, image):
    print(length * image)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    times = 0
    while times < size:
        line(size, "#")
        times += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)

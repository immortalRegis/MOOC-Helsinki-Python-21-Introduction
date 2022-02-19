# Copy here code of line function from previous exercise and use it in your solution
def line(length, image):
    print(length * image)

def triangle(size, character):
    # You should call function line here with proper parameters
    i = 1
    while i <= size:
        line(i, character)
        i += 1

def bottom(height, width, character):
    # You should call function line here with proper parameters
    i = 0
    while i < height:
        line(width, character)
        i += 1

def shape(top, character, base, symbol):
    triangle(top, character)
    bottom(base, top, symbol)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
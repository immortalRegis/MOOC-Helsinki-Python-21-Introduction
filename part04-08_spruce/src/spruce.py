# Write your solution here
def spruce(height):
    num = height
    space_count = num - 1
    stars_count = 1
    print("a spruce!")
    while num > 0:
        print(space_count * " " + (stars_count * "*"))    
        space_count -= 1
        stars_count += 2
        num -= 1
    print((height - 1)*" " + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
# Write your solution here
def create_tuple(x: int, y: int, z: int):
    first = min(x, min(y, z))
    second = max(x, max(y, z))
    third = x + y + z

    return (first, second, third)


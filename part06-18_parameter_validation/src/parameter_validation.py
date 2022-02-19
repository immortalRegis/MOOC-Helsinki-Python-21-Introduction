# Write your solution here
def new_person(name: str, age: int):
    if len(name) == 0:
        raise ValueError("Name cannot be an empty string")
    if len(name.split()) < 2:
        raise ValueError("At least 2 names must be provided")
    if len(name) > 40:
        raise ValueError("Too many characters in name")
    if age < 0 or age > 150:
        raise ValueError("Age is out of acceptable range")
    
    return (name, age)
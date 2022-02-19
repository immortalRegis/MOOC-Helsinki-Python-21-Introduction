# Write your solution here
import json
def print_persons(filename: str):
    with open(filename) as my_file:
        data = json.loads(my_file.read())
    
    for info in data:
        name = info["name"]
        age = info["age"]
        hobbies = ""
        for hobby in info["hobbies"]:
            hobbies += (hobby + ", ")
        
        hobbies = hobbies[0:(len(hobbies) - 2)]
        
        print(f"{name} {age} years ({hobbies})")


if __name__ == "__main__":
    print_persons("file1.json")

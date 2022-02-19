# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    instruction = int(input("Function: "))
    if instruction == 0:
        break
    elif instruction == 1:
        entry = input("Diary entry: ")
        new_entry = entry + "\n"
        with open("diary.txt", "a") as diary:
            diary.write(new_entry)
            print("Diary saved")
        print()
    
    elif instruction == 2:
        print("Entries")
        with open("diary.txt") as diary:
            for entry in diary:
                print(entry.strip())
print("Bye now!")
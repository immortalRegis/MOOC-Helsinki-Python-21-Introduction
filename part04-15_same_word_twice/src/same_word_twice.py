# Write your solution here
holder = []
count = 0
while True:
    word = input("Word: ")
    if word in holder:
        break
    holder.append(word)
    count += 1
print(f"You typed in {count} different words")
# Write your solution here
holder = []
while True:
    item = int(input("New item: "))
    if item == 0:
        break
    holder.append(item)
    print(f"The list now: {holder}")
    ordered_holder = sorted(holder)
    print(f"The list in order: {ordered_holder}")
print("Bye!")
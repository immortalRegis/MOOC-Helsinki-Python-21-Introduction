# Write your solution here
times = int(input("How many items: "))
holder = []
i = 1

while i <= times:
    item = int(input(f"Item {i}:"))
    holder.append(item)
    i += 1

print(holder)
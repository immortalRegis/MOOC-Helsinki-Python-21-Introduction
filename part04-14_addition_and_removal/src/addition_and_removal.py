# Write your solution here
holder = []

while True:
    print(f"The list is now {holder}")
    operation = input("a(d)d, (r)emove or e(x)it: ")

    if operation == "x":
        break
    
    
    if operation == "d":
        value = len(holder) + 1
        holder.append(value)
        continue
    
    if operation == "r":
        holder.pop()
        
print("Bye!")
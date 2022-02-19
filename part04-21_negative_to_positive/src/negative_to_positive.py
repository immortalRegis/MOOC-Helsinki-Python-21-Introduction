# Write your solution here
number = int(input("Please type in a positive integer: "))
negative_number = -1 * number
limit = number + 1

for i in range(negative_number, limit):
    if i == 0:
        continue
    print(i)
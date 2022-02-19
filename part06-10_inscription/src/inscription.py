# Write your solution here
name = input("Who should I sign this to: ")
filename = input("Where shall I save it to: ")

with open(filename, "w") as new_file:
    new_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")


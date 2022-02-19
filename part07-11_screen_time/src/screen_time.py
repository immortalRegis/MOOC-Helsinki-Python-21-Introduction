# Write your solution here
from datetime import datetime, timedelta

file_name = input("File name: ")
given_date = input("Starting date: ")
start_date = datetime.strptime(given_date, "%d.%m.%Y")

duration = int(input("How many days: "))
total_minutes = 0
minutes_per_day = {}

for i in range(duration):
    day = timedelta(days = i)
    ex_day = start_date + day
    exact_day = datetime.strftime(ex_day, "%d.%m.%Y")
    min_for_day = input(f"Screen time {exact_day}: ")
    mins = min_for_day.split(" ")

    print("Please type in screen time in minutes on each day (TV computer mobile):")

    for stored_min in mins:
        total_minutes += int(stored_min)
    
    current_mins = min_for_day.replace(" ", "/")
    
    minutes_per_day[exact_day] = current_mins

average_time = 0
if duration > 0:
    average_time = float(total_minutes) / duration
starting_time = datetime.strftime(start_date, "%d.%m.%Y")

with open(file_name, "w") as new_file:
    new_file.write(f"Time period: {starting_time}-{exact_day}" + "\n")
    new_file.write(f"Total minutes: {total_minutes}" + "\n")
    new_file.write(f"Average minutes: {average_time:.1f}"  + "\n")
    
    for key, value in minutes_per_day.items():
        new_file.write(f"{key}: {value}" + "\n")

print("Data stored in file late_june.txt")    



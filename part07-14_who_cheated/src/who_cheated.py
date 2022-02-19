# Write your solution here
from datetime import datetime, timedelta

def cheaters():
    cheaters = []
    start = {}
    stop = {}


    with open("start_times.csv") as file_name, open("submissions.csv") as stop_file:
        # read name and start times into {} 'start'
        for line in file_name:
            line = line.strip()
            row = line.split(";")
            start[row[0]] = row[1]

        # read all the stop times for each person into a [] 'stop'
        for line in stop_file:
            line = line.strip()
            row = line.split(";")
            if row[0] in stop:
                stop[row[0]].append(row[3])
            else:
                stop[row[0]] = []
                stop[row[0]].append(row[3])
            
            # find the difference between the individual times of a person and the start time.
            # if any of the differences between times is more than 3 hours, add the person to cheat list
        for key, value in stop.items():
            start_time = datetime.strptime(start[key], "%H:%M")
            stored_times = value
            limit = timedelta(hours=3)
            for st in stored_times:
                stop_time = datetime.strptime(st,"%H:%M")
                difference = stop_time - start_time
                if difference > limit and key not in cheaters:
                    cheaters.append(key)

        return cheaters
            
if __name__ == "__main__":
    print(cheaters())



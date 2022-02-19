# Write your solution here
from datetime import datetime, timedelta
def final_points():
    start = {}
    points_holder = {}
    total_points = {}

    with open("start_times.csv") as file_name, open("submissions.csv") as stop_file:
        # read name and start times into {} 'start'
        for line in file_name:
            line = line.strip()
            row = line.split(";")
            start[row[0]] = row[1]

        # find difference between start and stop time for each submission. If > 3, ignore scores
        for line in stop_file:
            line = line.strip()
            row = line.split(";")
            
            start_time = datetime.strptime(start[row[0]], "%H:%M")
            stop_time = datetime.strptime(row[3],"%H:%M")
            accepted_duration = timedelta(hours=3)
            difference = stop_time - start_time
            if difference > accepted_duration:
                continue

            current_scores = {}
            current_scores[row[1]] = row[2]
            
            if row[0] in points_holder:
                stored_scores = points_holder[row[0]]
                if row[1] in stored_scores:
                    a = stored_scores[row[1]]
                    if int(a) < int(row[2]):
                        stored_scores[row[1]] = row[2]
                else:
                    stored_scores[row[1]] = row[2]
            else:
                points_holder[row[0]] = {}
                points_holder[row[0]] = current_scores
        
        total = 0     
        for key in points_holder:
            value = points_holder[key]
            for k,v in value.items():
                total += int(v)
            total_points[key] = total
            total = 0
        
        return total_points



            
if __name__ == "__main__":
    print(final_points())



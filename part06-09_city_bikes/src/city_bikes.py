# tee ratkaisu tänne
# Write your solution here
import math
def get_station_data(filename: str):
    station_info = {}
    with open(filename) as new_file:
        for row in new_file:
            row = row.strip()
            info = row.split(";")
            if info[3] == "name":
                continue
            long = float(info[0])
            lat = float(info[1])
            station_info[info[3]] = (long, lat)
    
    return station_info


def  distance(stations: dict, station1: str, station2: str):
    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]
    latitude1 = stations[station1][1]
    latitude2 = stations[station2][1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    holder = []
    for station in stations:
        if station == "name":
            continue
        holder.append(station)
    
    s1 = ""
    s2 = ""
    gd = 0
    
    for i in range(len(holder)):
        for j in range(i + 1, len(holder)):
            d = distance(stations, holder[i], holder[j])
            if d > gd:
                s1 = holder[i]
                s2 = holder[j]
                gd = d
    
    return (s1, s2, gd)
        


if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    for station in stations:
        print(station)

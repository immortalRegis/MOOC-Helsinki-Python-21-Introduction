# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    new_entry = {}
    new_entry["name"] = name
    new_entry["director"] = director
    new_entry["year"] = year
    new_entry["runtime"] = runtime

    database.append(new_entry)
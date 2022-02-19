# Write your solution here
def find_movies(database: list, search_term: str):
    found_movies = []

    for movie_entry in database:
        if search_term.lower() in movie_entry["name"].lower():
            found_movies.append(movie_entry)

    return found_movies
import csv
import re

try:
    with open("movies.csv", "r") as file:
        reader = csv.DictReader(file)
        movies = list(reader)

    print("All Movie Information:")
    for movie in movies:
        print(movie)

    movie_id = input("\nEnter Movie ID to search: ")

    found = False

    for movie in movies:
        if movie["Movie ID"] == movie_id:
            print("\nMovie Found:")
            for key, value in movie.items():
                print(f"{key}: {value}")
            found = True
            break

    if not found:
        print("Movie not found.")

    title = input("\nEnter title to search: ")

    print("\nMovies matching the title:")
    found_title = False

    pattern = re.compile(title, re.IGNORECASE)

    for movie in movies:
        if pattern.search(movie["Title"]):
            print(movie)
            found_title = True

    if not found_title:
        print("No movies found with that title.")

except FileNotFoundError:
    print("Error: movies.csv file not found.")
except Exception as e:
    print("Error:", e)

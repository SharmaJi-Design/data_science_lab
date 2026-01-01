# Q.1. Movie Ratings Analyzer 
# Ask the user to input a list of movies with ratings like [("Titanic", 8), ("Inception", 9), ...]. Compute 
# the average rating, find the highest-rated movie, and list all movies with rating above the average. 

user_input = input("Enter movies and ratings: ")

movies = []
items = user_input.split(',')

for item in items:
    if '-' in item:
        name, rating = item.split('-')
        name = name.strip()
        rating = float(rating.strip())
        movies.append((name, rating))

total = sum(rating for name, rating in movies)
average = total / len(movies)
highest_rating = max(rating for name, rating in movies)

above_avg = [(name, rating) for name, rating in movies if rating > average]
below_avg = [(name, rating) for name, rating in movies if rating < average]

print("Average Rating:", round(average, 2))
print("Highest Rating:", highest_rating)
print("Movies Above Average:", above_avg)
print("Movies Below Average:", below_avg)
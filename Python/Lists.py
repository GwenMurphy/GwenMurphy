import random

fav_movies = ["Charlie's Angels (2019)", "Avengers: Endgame", "Doctor Strange", "Avengers: Infinity War"]

# print(fav_movies)     Prints whole list.
print(fav_movies[0])

"""
Individual items can be grabbed from the list.
Involves square brackets. Printing the first item would be
        print(favour(fav_movies[0])
as it starts 0, 1, 2, ..., n.
"""

fav_numbers = [16, 69, 420]

print(fav_numbers[random.randint(0,2)])

# To find list length         print(len(fav_movies))
print(len(fav_movies))

# To add to list              fav_movies.append('FILM NAME')
fav_movies.append('Hitchhiker\'s Guide to the Galaxy')
print(fav_movies)

#To Insert
fav_movies.insert(1, 'Filmy McFilmFace')
print(fav_movies)

#For loop
for x in fav_movies:
    print(x)
    
#To delete
del(fav_movies[1])
print(fav_movies)
# # 1. Creat a program that has a function that will multiply two numbers together and print out the results.

# # Make the program properly handle an exception if something besides a number is passed as an argument.
# # Have it print out 3 different sets of numbers
# print("****1****")

# def multiply_two_numbers(a, b):
#     print(a * b)

# for i in range(1, 4):
#     while True:
#         try:
#             user_number_a = int(input("\nGive me any number.\n"))
#             user_number_b = int(input("\nLet's have a second number.\n"))
#             break
#         except ValueError:
#             print("*****Please choose a number.*****")
#     print("\nThe product is: ")
#     multiply_two_numbers(user_number_a, user_number_b)


# 2. Create a program that has a function that will accept 3 arguments as title, genre, year and then print out the values in list format.

#     1. Title : Star Wars - A new Hope
#     2. Genre : Sci-Fi
#     3. Year  : 1977
# print("*****2*****")

# def movie(title, genre, year):
#     print(f"1. Title: {title}")
#     print(f"2. Genre: {genre}")
#     print(f"3. Year: {year}")

# movie("Never Ending Story", "Fantasy", 1984)


# 3. Create a program that does the same thing as above, but the function only accepts a single argument to get the same results.
# (hint) - You will need to use a datatype other than a string in the argument.
print("****3****")

movies = {
    "title" : "Never Ending Story",
    "genre" : "Fantasy",
    "year" : "1984"
}

movie = {
    "title":"Star Wars",
    "episode":4,
    "year":"1977",
    "villains":["Vader", "Tarkin"],
    "heros":["Luke","Leia", "Han", "Obi-Won"],
    "genre" : "Sci-Fi"
}



def movies_funct(d):
    print(f"1. Title: {d['title']}")
    print(f"2. Genre: {d['genre']}")
    print(f"3. Year: {d['year']}")

movies_funct(movies)
movies_funct(movie)


# ***This throws an Error***
# movie_2 = {
#     "SW": {"title" : "Star Wars",
#     "episode":4,
#     "year":"1977",
#     "villains":["Vader", "Tarkin"],
#     "heros":["Luke","Leia", "Han", "Obi-Won"],
#     "genre" : "Sci-Fi"},
#     "NES" : {"title" : "Never Ending Story",
#     "genre" : "Fantasy",
#     "year" : "1984"}
# }
# movies_funct(movie_2)

print("****Clint****") #<---When you might not have all of the info you want!

def movie(movie_item):
    idx = 1 #<---This resets the idx when the function is rerun....
    for item in movie_item:
        print(f"{idx}. {item} : {movie_item[item]}")
        idx += 1

movie({"Genre":"Horror", "Title" : "Clint at the Beach", "year" : 2020})

movie({"Nothing" : "No Movies"})


# Key Value Pairs

# Dictionary - In python, a dictionary is a data type that is a grouping of data that uses keys to point to a value. Some languages have data types that are similer called things like maps, structs, or objects.
# Key - In programming, a key is string, int, or one of a varity of data types that will allow the developer to access a value.

  # Key value pairs in python are dictionaries
movie = {
    "name":"Star Wars",# Key is name, value is Star Wars!
    "episode":4, #key is episode, value is 4
    "year":"1977"
}
#### We are using curly brackets, not crotchets!

#Dictionaries can have multipe data types as values
movie = {
    "name":"Star Wars",
    "episode":4,
    "year":"1977",
    "villains":["Vader", "Tarkin"],
    "heros":["Luke","Leia", "Han", "Obi-Won"]
}

#print from dictionary
print(movie["name"]) 
#assign to variable
bad_guys = movie["villains"]
print(bad_guys)
print(bad_guys[1])
bad_guys.append("Jabba")
print(movie)


#accessing a value from an array in the dictionary
print(movie["heros"][1]) #Leia
#  capitalization matters!

# the key can be a variable
search = "villains"
print(movie[search])
# If you use this with user input and they do not put in a key that works,
# They will get a KeyError!
# A way to prevent the error:
#check for existance
if "ships" in movie:
    print(movie["ships"])
else:
    print("Item not found")

# if not
if "ships" not in movie:
    print("We need to add ships")    

# if you append a dictionary, you append the original. But if you make a set first, it pulls the items and then you can put it back as a list and append it wihtout altering the orig.

#adding to the current string
movie["name"] = movie["name"]+" - A new Hope"

#Adding a new item
movie["ships"] = ["Falcon", "Star Destroyer", "Death Star"]

#Adding to an element inside of an list
movie["heros"].append("Chewbacca")
print(movie["heros"])

print("************")
for key in movie:
    print(key) #Just prints the keys


for key in movie:
    print("*****NEXT ITEM*****")
    print(movie[key]) #the key is a variable
    # you could also say print(key, movie[key]) to get the key to print in front
    print(f"{key} :", movie[key])

movies = [
      {
          "name":"Star Wars - A new Hope",
          "episode":4,
          "year":"1977"
      },
      {
          "name":"Star Wars - The Empire Strikes Back",
          "episode":5,
          "year":"1980"
      },
      {
          "name":"Star Wars - Return of the Jedi",
          "episode":6,
          "year":"1983"
      }
  ]
#get item from list
print(movies[0]["name"])

#loop through list of dictionaries
for movie in movies:
    print("%s was episode %s and release in %s" % (movie["name"], movie["episode"], movie["year"]))


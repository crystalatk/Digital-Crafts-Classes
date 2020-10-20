# 1. Write a program that has a list of shopping lists that 
    # where each list is for a different food group.
#       Print each full list on a seperate line.
#       ['Corn','Potatoes','Tomatoes']
#       ['milk','eggs','cheese','yogurt']
#       ['frozen pizza','popsicle']
print("****1****")
food_list = [
    ['Corn','Potatoes','Tomatoes'],
    ['milk','eggs','cheese','yogurt'],
    ['frozen', 'pizza','popsicle']
]
print(f"{food_list[0]}\n{food_list[1]}\n{food_list[2]}")


# 2. Using the code from the previous exercise, have each 
    # grouping have a title with the number in the title and 
    # each item of the list have a number in front of the item.
#       (bonus) Have each of the titles of the main grouping 
#       be in a seperate list that gives the name to the heading.
        # 1. Veggies
        #     1. Corn
        #     2. Potatoes
        #     3. Tomatoes
        # 2. Cold Items
        #     1. milk
        #     2. eggs
        # ...etc
print("***2***")


stuff = ["Veggies", "Cold", "Frozen"]
counter = 0

for titles in stuff:
    print(f"{counter +1}. {titles}")
    idx = 1
    for food in food_list[counter]:
        print(f"\t{idx}. {food}")
        idx += 1
    counter += 1


# ****WRONG WAY******
# while food_list:
#     id = 0
#     print(f"{id + 1}. Veggies")
#     while len(food_list[id]):
#         count = 1
#         id_0 = 0
#         print(f"\t{count}. {food_list[id][id_0]}")
#         del food_list[id][id_0]
#         count += 1
#         print(f"{id + 1}. Veggies")
#     id += 1
#     print(f"{id + 1}. Cold Items")
#     while food_list[id]:
#         count = 1
#         id_0 = 0
#         print(f"\t{count}. {food_list[id][id_0]}")
#         del food_list[id][id_0]
#         count += 1
#     id += 1
#     print(f"{id + 1}. Frozen Items")
#     while food_list[id]:
#         count = 1
#         id_0 = 0
#         print(f"\t{count}. {food_list[id][id_0]}")
#         del food_list[id][id_0]
#         count += 1



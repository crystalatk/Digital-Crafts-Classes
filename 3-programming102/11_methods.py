  #in game terms mob stands for mobile. It can be anything that moves including enemies, npc, and the player's characters.
class Mob:
    def __init__(self, name, health = 10, power=2):#As a rul, this one comes first(init)
        self.name = name
        self.health = health
        self.power = power
    #You could replace the arguments with a dictionary (you would use arg and then do arg.health, arg.power, etc....)
    # The first argument of every method is self.******
    def get_hit(self, power):
        self.health = self.health - power
        print('I, %s, have been hit for %s points and now my health is %s!' % (self.name, power, self.health))#Could use f-string to insert here...
        # return self.health #You can return a value so that you can use it outside of the class!

    def attack(self, enemy):
        enemy.get_hit(self.power)#self power is the power of the original hitter! Not enemy


#The order of the methods doesn't matter. 
#Methods are just functions inside of a class...

bad_guy = Mob("Evil McEvil", 10, 3)
hero = Mob("Sir Galahand", 30, 10)
#self is not placed here. The class handles that itself
# print(hero.health)
# hero.get_hit(2)
# print(hero.health)
# # print("****")
# # look = hero.get_hit(6)#If you make a return, you can use that return value
# # print(look)
# # print("***")
# print(bad_guy.health)
# hero.get_hit(2)
# print(hero.health)

bad_guy.attack(hero)
bad_guy.attack(hero)
hero.attack(bad_guy)

# IF you wanted to use a dictionary
# hero = Mob({
#     name: "Clint",
#     health: 20,
# })
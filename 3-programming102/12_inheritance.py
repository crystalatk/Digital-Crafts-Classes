# # Using inheritance create a subclass
 
#  # Previous class lesson without print text
# class Mob:
#     def __init__(self, name, health = 10, attack_power = 2):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power 

#     def get_hit(self, power):
#         self.health = self.health - power            

#     def attack(self, enemy):           
#         enemy.get_hit(self.attack_power)

# #not very useful but valid
# class Hero(Mob):#Hero class is a sublclass of Mob 
#     def yell(self):
#         print("I, %s, say to thou villan. Prepare to die!" % self.name)


# hero = Hero("Clint", 60, 6)
# bad_guy = Mob("Baddy")
# hero.yell()
# hero.attack(bad_guy)
# print(bad_guy.health)

## Overriding Class Method!

# Previous class lesson without print text
class Mob:
    def __init__(self, name, health = 10, attack_power = 2):
        self.name = name
        self.health = health
        self.attack_power = attack_power 

    def get_hit(self, power):
        self.health = self.health - power            

    def attack(self, enemy):           
        enemy.get_hit(self.attack_power)


class Hero(Mob):
    #overriding __init__
    def __init__(self):
        super().__init__("Sir Barksalot", 22, 3)#Calls from the parent init
        self.defense = 1

    def get_hit(self, power):
        print("Hey, y'all. I'm getting hit! It hurts.")
        # self.health = self.health - power
        super().get_hit(power-self.defense)
        if self.defense >= power/2:
            print("Ha Ha! My defense is GREAT!")
    def yell(self):
        print("I, %s, say to thou villan. Prepare to die!" % self.name)
    
#supers call a function from the parent even if the parent has been overridden...
# You can have multiple levels down
class Creature(Mob):
    def grunt(self):
        print("grbrgrb")

class Orc(Creature):
    def stomp(self):
        print("I'm going to stomp!")

hero = Hero()
bad_guy = Orc("Baddy")
hero.yell()
hero.attack(bad_guy)
print(bad_guy.health) 

bad_guy.stomp()
print(hero.health)

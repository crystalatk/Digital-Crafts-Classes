class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.')
    def hello(self, test):
        print(f"This is a {test}.")

class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        # self.NonWingedMammal = NonWingedMammal
        self.reason = "They are non-winged because "
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)
    def printagain(self, Vble):
        print(f"{self.reason} {Vble}.")

class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        self.legs = 4
        print(f'Dog has {self.legs} legs.')
        super().hello("yep!")
        super().__init__('Dog')
        super().printagain(f'they use {self.legs} legs')
        
    def printname(self):
        print("This is a dog")

class Snake(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        self.legs = "no"
        print("Snakes have no legs.")
        super().__init__("Snakes")
        super().printagain(f"they slither with {self.legs} legs")
        
    def choice(self, user_choice):
        if user_choice == "black":
            print("You die")
        else:
            print("You live")


# r = {"dogs" : Dog(), "snakes" : Snake()}
# # d = Dog()
# print('')
# # bat = NonMarineMammal('Bat')
# # d.printname()
# # d.printagain("bobcat")
# # r = Dog()
# # print('')
# # s = Snake()
# user_choice = input("What would you like to talk about? dogs or snakes?")
# for key in r:
#     if user_choice.lower() == key:
#         print(key)
#         print(r[key])
#         animal = r[key]
# animal.printname()
# animal.printagain("funky")

# d= Dog()

s = Snake()
user_choice = input("Do you like black, red, or brown snakes?")
d = s.choice(user_choice)

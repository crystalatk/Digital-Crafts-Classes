# Create a program that has a class named Vehicle.
#   Make the Vehicle have a 'category' attribute which can be anything like, sport, truck, motorcycle, minivan.
#   Make the Vehicle class have 'wheels' as an attribute.
#   Make the Vehicle class have 4 as the default value for the class.
#   Create 5 different instances of the class with at least one being a motorcycle.

class Vehicle:
    def __init__(self, category, wheels="4"):
        self.category = category
        self.wheels = wheels

motorcycle = Vehicle("motorcycle", 2, )
truck = Vehicle("truck")
sport = Vehicle("sport")
luxury = Vehicle("luxury")
bus = Vehicle("bus", 6)

print(motorcycle.wheels)
print(bus.wheels)
# Using our vehicle class from the previous lesson, add a speed, top_speed, position, and acceleration attribute.
#   speed and position should start at 0, top_speed and acceleration are numbers.
#   add a class method called move. When the move method is called have the position increase by the speed of the car.
#   add a class method called accelerate and using the very simplified equation to have the vehicle accelerate when the accelerate method is called on that instance:
#        speed = speed + acceleration
#   In the accelerate method, do not allow the vehicle to pass the top speed.
#   modify the instances of the vehicles to include acceleration and top speed when you instance the vehicles.
#   using a while loop and assuming each iteration of the loop is a 'second' have the vehicles 'race' by accelerating as much as possible on a drag strip for 20, 40, and 60 seconds to see who wins.
#   (challange) instead of racing for a timeframe, make the race different distances. Position can be considered in meters.

import time

class Vehicle:
    def __init__(self, category,  top_speed,  acceleration, wheels=4):
        self.category = category
        self.wheels = wheels
        self.acceleration = acceleration
        self.top_speed = top_speed
        self.speed = 0
        self.position = 0
        self.race_stats = []
    
    def move(self):
        self.position += self.speed
    
    def accelerate(self):
        # print(self.category, self.speed)
        self.speed += self.acceleration
        if self.speed > self.top_speed: 
            self.speed = self.top_speed
        self.move()
        self.race_stats.append({"speed" : self.speed, "position" : self.position})
        return self.speed
    
    def reset(self):
        self.position = 0
        self.speed = 0
    
    def start_race(self):
        self.race_stats.append([])



motorcycle = Vehicle("motorcycle", 100, 11, 2)
truck = Vehicle("truck", 120, 5)
sport = Vehicle("sport", 150, 10)
luxury = Vehicle("luxury", 130, 8)
bus = Vehicle("bus", 60, 2, 6)

all_racers = [motorcycle, truck, sport, luxury, bus]
n = 1
seconds = 20
while n < seconds:
    for v in all_racers:
        v.accelerate()
    n += 1
for v in all_racers:
    print(f"{v.category} went {v.position} and reached {v.speed} speed.")


# print(f"And the results are: {order}")

all_cars = {
    "motorcycle" : Vehicle("motorcycle", 100, 11, 2),
    "truck" : Vehicle("truck", 120, 5),
    "sport" : Vehicle("sport", 150, 10),
    "luxury" : Vehicle("luxury", 130, 8),
    "bus" : Vehicle("bus", 60, 2, 6),
}


print("20 second run!")

def run_race(seconds):
    for car_name in all_cars:
        all_cars[car_name].reset()
        all_cars[car_name].start_race()

    i = 0
    while i < seconds:
    # for sec in range(seconds +1):
        # print(f"Second {sec}")
        for car_name in all_cars:
            all_cars[car_name].accelerate()
        i += 1
    print("Race is Over!")
    # time.sleep(3) #<----this will cause a 3 second delay. Will freeze the program! Usually don't.
    for car_name in all_cars:
        print(f"{car_name} - {all_cars[car_name].position}")
        

# for car_name in all_cars:
#     print(f" {car_name}:")

run_race(20)

print("40 seconds")

run_race(40)

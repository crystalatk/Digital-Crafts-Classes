// 1.Create an object called 'spaceship'.
// give it the following keys with whatever values seems reasonable to you. speed,acceleration, passangers, fuel.

let spaceship = {
  speed: 135,
  acceleration: 15,
  passengers: 10,
  fuel: 120,
};

// 2. Using the spaceship object above add a payload key after the object has been created. (just give it a number)

spaceship.payload = 32;

console.log("\n\n#2");
console.log(spaceship);

// 3. Using the same object above, lower the amount of fuel by 1/3.

spaceship.fuel = spaceship.fuel - spaceship.fuel / 3;

console.log("\n\n#3");
console.log(spaceship.fuel);

// 4. loop through the object and give a message to the console like the one below for every property in the object.
//    passangers : 100
//    ...

console.log("\n\n#4");
for (attrib in spaceship) {
  if (!spaceship.hasOwnProperty(attrib)) continue;
  console.log(`${attrib} : ${spaceship[attrib]}`);
}

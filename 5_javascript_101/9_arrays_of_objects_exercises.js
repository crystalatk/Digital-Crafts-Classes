// Make an array of ship objects (at least 3). Each ship needs a name, topSpeed, acceleration, and cargo capacity.
// 1. console.log the name and top speed of the 2nd ship.
// 2. loop through the array and print out every stat in a key:value style.
// 3. (Bonus) sort the array by the ship with the fastest speed and console log it out.

let shipArray = [
  {
    name: "Star",
    topSpeed: 200,
    acceleration: 20,
    cargoCapacity: 8,
  },
  {
    name: "Moon",
    topSpeed: 50,
    acceleration: 5,
    cargoCapacity: 200,
  },
  {
    name: "Saturn",
    topSpeed: 250,
    acceleration: 150,
    cargoCapacity: 3,
  },
];
console.log(shipArray);

console.log("#1");
console.log(shipArray[1].name + " : " + shipArray[1].topSpeed);

console.log("\n\n#2");
shipArray.forEach(function (ship) {
  console.log("name : " + ship.name);
  console.log("topSpeed : " + ship.topSpeed);
  console.log("acceleration : " + ship.acceleration);
  console.log("cargoCapacity : " + ship.cargoCapacity);
});
shipArray.forEach(function (ship) {
  for (key in ship) {
    console.log(`${key} : ${ship[key]}`);
  }
  console.log("******");
});

console.log("\n\n#3");
console.log(shipArray.sort(shipArray.topSpeed));

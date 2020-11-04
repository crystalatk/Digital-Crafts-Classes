// 1. Instance an object of any name of your choice.

function Pizza(type, toppings, size) {
  this.type = type;
  this.toppings = toppings;
  this.size = size;
}

let VegCal = new Pizza("Vegan", "Banana Peppers & Spinach", "10 inch");

console.log(VegCal.type);

// 2. Using the mdn documents about Array, check to see if that instance is an array.
// create an array and check to see if it is an array as well.

console.log(Array.isArray(VegCal));

let myArray = [1, 2, 3, 4];

console.log(Array.isArray(myArray));

// 3. Using the documents join the array together and console.log the results.

console.log(myArray.join(" "));

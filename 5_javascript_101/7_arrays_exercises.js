// Create a list of letters at with at least 10 items.
// print the 4th item.
// concatinate the 6th and 3rd item and print the results.
// add 4 more letters one at a time to the end of the array.
// remove the first item of the array.
// join all of the letters together and send the results to the console.
// (bonus) sort the letters!

let myArray = ["a", "c", "d", "e", "f", "g", "z", "r", "ty", "u", "o"];
console.log(myArray[3]);

console.log(myArray[5] + myArray[2]);

myArray.unshift("y", "p", "w", "qu");
console.log(myArray);

myArray.shift();
console.log(myArray);

let joint = "";

myArray.forEach(function (value) {
  joint += value;
  return joint;
});

console.log(joint);

console.log(myArray.join("")); //the empty string makes them just be together. If you put things in the string, it will put things between the letters.

console.log(myArray.join("-"));

console.log(myArray.join("-letter-"));

myArray.sort();

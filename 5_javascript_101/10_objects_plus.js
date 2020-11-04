// // Terms

// // typeof - in javascript typeof is an operator to output what data type an item is.
// // instanceof - In javascript instanceof is an operator that will compare a value with a given object to see if it is an instance of that object
// // In javascript everything is (or at least can be) an object. Even Strings, Numbers, Booleans. Don't sweat it its odd but it doesn't have to be confusing.

// console.log(typeof "yes"); //string
// console.log(typeof new String("yes")); //object

// let myString = "yes";
// let anotherString = new String("yes");

// console.log(myString, myString.length);
// console.log(anotherString, anotherString.length);

// "yes" instanceof Object; //false
// new String("yes") instanceof Object; // true

// function test() {}

// console.log(typeof test); //function
// test instanceof Object; //true

// // Functions are objects. We call them first class objects in javascript.

// // Creating instance with new

// function Animal() {}
// let rainbow = Animal(); //undefined
// //Animal as a function doesn't return anything

// //creating an instance
// rainbow = new Animal();
// console.log(rainbow); //instance of Animal

// Convention says if it is a object to be instanced you capatalize it.

// This

// function Animal(type, name) {
//   this.name = name;
//   this.type = type;
// }
// // let shadow = new Animal("cat", "shadow");
// console.log(shadow);
//adding methods
// function Animal(type, name, noise) {
//   this.name = name;
//   this.type = type;
//   this.noise = noise;
//   this.makeNoise = function () {
//     console.log(this.name + " says " + this.noise);
//   };
// }

// let shadow = new Animal("cat", "shadow", "meow");
// console.log(shadow);
// console.log("***");
// shadow.makeNoise();

// // this is like self for python, but it is a keyword and not an argument. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new

// for (attrib in shadow) {
//   console.log(attrib);
// }

// Prototype

function Animal(type, name, noise) {
  this.name = name;
  this.type = type;
  this.noise = noise;
}

Animal.prototype.makeNoise = function () {
  console.log(this.name + " says " + this.noise);
};
// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes

let shadow = new Animal("cat", "Shadow", "Grrr");

shadow.makeNoise();

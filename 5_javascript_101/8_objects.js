// Creating Objects

//empty object
let myObj = {};

//object with values: keys are made into strings, so they do not need to have quotes.
let aboutMe = {
  name: "Clint",
  age: 38,
  tall: false,
};

//   You can, this is like python
console.log(aboutMe["name"]);

let seachBy = "name";

console.log(aboutMe[seachBy]);

// Or you can do the dot notation! These are treated like classes: more standard way unless the key you are searching for is a variable
console.log(aboutMe.name);

//using new
let another = aboutMe;
console.log(another);

// Accessing Values

//like python
console.log(aboutMe["name"]);
//keys must be strings ... technically
// so they can be accessed via dot notation.
console.log(aboutMe.name);

// Modifying values

//from above
//changing a key
aboutMe.name = "Clint F";
console.log(aboutMe);

//adding new key
aboutMe.gender = "Male";
console.log(aboutMe);

//removeing a key
delete aboutMe.tall;
console.log(aboutMe);

// Looping through an object

let aboutYou = {
  name: "Clint",
  age: 38,
  tall: false,
};

//for in loop
for (attrib in aboutYou) {
  console.log(attrib);
  console.log(aboutYou[attrib]);
}

//technically this is better because of some quirkiness of js inheritance situations: Use this in case there are thousands of other keys, if it doesn't have attrib then it will move on.
for (attrib in aboutYou) {
  if (!aboutMe.hasOwnProperty[attrib]) continue; //****Do this step!!!! */
  console.log(attrib);
  console.log(aboutYou[attrib]);
}
// Better ways to loop through objects will be discussed in es6

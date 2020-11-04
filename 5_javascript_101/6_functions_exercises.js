// Write a function that accepts 3 arguments and returns the value of all the items added together.

function printNumbers(one, two, three) {
  return one + two + three;
}

console.log(printNumbers(3, 5, 6));

// Write a function that has an anonymous function as the first argument and a number as the second argument.

// the anonymous function needs to console.log something.
// Have the first function count from 0 to the number that the second argument is.
// After it is done counting have it call the anonymous function.
// call the function again with a different function as the argument.

const thisThing = function (single) {
  console.log("This is confusing");
};

function newFunction(noOneKnows, number) {
  let i = 0;
  while (i <= number) {
    console.log(i);
    i++;
  }
  noOneKnows();
}

newFunction(thisThing, 10);

newFunction(function () {
  console.log("Are we still doing this?");
  console.log("I think I got it!");
}, 25);

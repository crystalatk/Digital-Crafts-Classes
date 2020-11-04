// Just the positives
// Write a function positiveNumbers which is given an array of numbers and returns a new array containing only the positive numbers within the given array.

// positiveNumbers([1, -3, 5, -3, 0])
// [1, 5, 0]
// positiveNumbers([1, 2, 3])
// [1, 2, 3]
// positiveNumbers([-1, -2, -3])
// []

function positiveNumbers(given) {
  let newArray = [];
  for (let i = 0; i < given.length; i++)
    if (given[i] >= 0) {
      newArray.push(given[i]);
    }
  return newArray;
}

console.log(positiveNumbers([1, -3, -4, 6, 3, 0, -10]));

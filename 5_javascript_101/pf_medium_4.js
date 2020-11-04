// # Print Numbers
// Write a function printNumbers which is given a start number and an end number. It will print the numbers from one to the other, one per line:

// printNumbers(1, 10)
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
// 10
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
// 10
// 11
// Write two versions of the above function. One using a while loop and the other using a for loop.

console.log("***For***");

function printNumbers(start, end) {
  for (let i = start; i <= end; i++) {
    console.log(i);
  }
}

printNumbers(2, 20);

console.log("***While***");

function printNumbersTwo(start, end) {
  let i = start;
  while (i <= end) {
    console.log(i);
    i++;
  }
}

printNumbersTwo(32, 38);

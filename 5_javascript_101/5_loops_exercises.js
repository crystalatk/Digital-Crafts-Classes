// Using a while loop add numbers from 1 to 10.

let num = 1;
let sum = 0;
while (num <=10){
    sum += num;
    num ++;
}
console.log(sum);

// Using a for loop, count from a number of your choice to another number.

for (let i = 1983; i < 2021; i++){
    console.log(i);
}


// Using a for loop, start with a number and then divide and replace that number by each number from 6 to 2.
// n = 300 //you choose a number
// ... // your code
// console.log(n) 
// //something like 0.000496031746031746

let n = 300;
for (let i = 6; i >=2; i--){
    n = n/i;
}
console.log(n);


// Using either type of loop add all of the numbers not divisible by 2 and 3 from 0 to a number of your choice.

let numChoice = 15;
let sumChoice = 0;

for (let i = 1; i <= numChoice; i++){
    if (!(i % 2) || !(i % 3)) sumChoice += i;
}

console.log(sumChoice);

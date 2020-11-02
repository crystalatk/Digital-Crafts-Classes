// Write a program that will declare a variable named "value".
// Have an if, if else, else statement that compares that value.

let value = 10

if(value === 8){
    console.log('value is 8')
} else if (value < 9){
    console.log('value must be 9')
} else {
    console.log('value is greater than 9')
}


// using ternary.
// compare if one number is greater than another.
// set the value of a variable named 'result' to 'higher' if the first number is higher and lower if the first number is lower.

let result

let firstNumber = 10
let secondNumber = 5

firstNumber > secondNumber ? result = 'higher': result = 'lower'

console.log(result)


// Using switch.
// set a variable named = 'temp' and give it a value between -20 & 110.
// Have cases for sub 0, 30, 50, 75, 80, 90, and above.
// Have a hex color for each level going from blue to red.
// print out the color that represents the range.
//     /* results */
//     temp = 50;
//     color = null;
//     ... //your code
//     console.log(color) //#cdff74 (kinda light green)

let temp = 73
let color = null

switch (true) {
    case (temp < 0):
       color = '#0000cc'
       break;
    case (temp< 30):
        color = '#0066ff'
        break;
    case (temp< 50):
        color = '#66ccff'
        break;
    case (temp< 75):
        color = '#ccffff'
        break;
    case (temp< 80):
        color = '#ffccff'
        break;
    case (temp< 90):
        color = '#ff6699'
        break;
    default:
        color = '#ff0000'
} 
console.log(color)
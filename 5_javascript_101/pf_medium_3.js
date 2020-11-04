// Tip Calculator 2
// Write a function totalAmount that takes the same arguments as tipAmount except it returns the total as the tip amount plus the bill amount. This function may make use of tipAmount as a sub-task.

// totalAmount(100, 'good')
// 120
// totalAmount(40, 'fair')
// 46

function totalAmount(bill, serviceLevel) {
  let tip = 0;
  if (serviceLevel == "good") tip = 0.2;
  else if (serviceLevel == "fair") tip = 0.15;
  else if (serviceLevel == "poor") tip = 0.1;
  return bill + bill * tip;
}

console.log(`$${totalAmount(100, "good")}`);

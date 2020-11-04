// Tip Calculator
// Write a function tipAmount that is given the bill amount and the level of service (one of good, fair and poor) and returns the dollar amount for the tip. Based on:

// good -> 20% fair -> 15% bad -> 10%

// tipAmount(100, 'good')
// 20
// tipAmount(40, 'fair')
// 6

function tipAmount(bill, serviceLevel) {
  let tip = 0;
  if (serviceLevel == "good") tip = 0.2;
  else if (serviceLevel == "fair") tip = 0.15;
  else if (serviceLevel == "poor") tip = 0.1;
  return tip * bill;
}
console.log(`$${tipAmount(10, "good")}`);

// Print a Banner
// Write a function printBanner which is given some text and prints a banner with a border surrounding the text. The border has to stretch to the length of the text.

// > printBanner('Welcome to DigitalCrafts')
// ----------------------------
// - Welcome to DigitalCrafts -
// ----------------------------

function printBanner(text) {
  console.log("-".repeat(text.length));
  console.log(text);
  console.log("-".repeat(text.length));
}

printBanner("- Welcome to DigitalCrafts -");

// Clint's solution
function printBanner(text) {
  let l = text.length;
  let s = "";
  for (let i = 0; i < l + 2; i++) s += "-";
  console.log(s);
  console.log("-" + text + "-");
  console.log(s);
}

printBanner("Women Belong in All Places");

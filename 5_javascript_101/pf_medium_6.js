// Print a box
// Write function printBox which is given a width and height and prints a hollow box of those given dimensions.

// printBox(6, 4)
//  ---
// |   |
//  ---

function printBox(width, height) {
  console.log(" - ".repeat(width));
  for (let i = 1; i < height - 1; i++) {
    console.log("|  " + "   ".repeat(width - 2) + "  |");
  }
  console.log(" - ".repeat(width));
}

printBox(7, 5);

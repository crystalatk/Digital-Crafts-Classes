// Leetspeak
// Write a function leetspeak which is given a string, and returns the leetspeak equivalent of the string. To convert text to its leetspeak version, make the following substitutions:

// A => 4 E => 3 G => 6 I => 1 O => 0 S => 5 T => 7

// leetspeak('Leet')
// l337
// let leetArray = [
//   ["A", "E", "G", "I", "O", "S", "T"],
//   [4, 3, 6, 1, 0, 5, 7],
// ];
// function leetspeak(phrase) {
//   let phraseUp = phrase.toUpperCase();
//   let phraseArray = phraseUp.split("");
//   for (let i = 0; i < phraseArray.length; i++) {
//     for (let j = 0; j < leetArray.length; j++)
//       if (phraseArray[i] == leetArray[0][j]) {
//         phraseArray[i] = leetArray[1][j];
//         break;
//       }
//   }
//   console.log(phraseArray.join(""));
// }

// leetspeak("fragile like a bomb");

let leetObject = { A: 4, E: 3, G: 6, I: 1, O: 0, S: 5, T: 7 };

function leetspeak(phrase) {
  let phraseArray = phrase.toUpperCase().split("");
  for (let i = 0; i < phraseArray.length; i++) {
    phraseArray[i] = leetObject[phraseArray[i]] || phraseArray[i];
  }
  console.log(phraseArray.join(""));
}

leetspeak("fragile like a bomb");

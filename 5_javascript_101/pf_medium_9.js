// Long-long Vowels
// Write a function, which is given a string, return the result of extending any long vowels to the length of 5.

// longLongVowels('Good')
// 'Goooood'
// longLongVowels('Cheese')
// 'Cheeeeese'
// longLongVowels('Man')
// 'Maaaaaaan'

function longVowel(word) {
  const vowels = ["A", "E", "I", "O", "U"];
  let wordArray = word.split("");
  for (let i = 0; i < wordArray.length; i++) {
    const letter = wordArray[i];
    for (let v = 0; v < vowels.length; v++) {
      if (letter.toUpperCase() == vowels[v] && letter == wordArray[i - 1]) {
        wordArray[i] = letter.repeat(4);
      }
    }
  }
  console.log(wordArray.join(""));
}

longVowel("goose");

// Caesar Cipher
// Write a function cipher which is given a string, an offset, and returns the Caesar cipher of the string.

// cipher('Genius without education is like silver in the mine')
// 'Travhf jvgubhg rqhpngvba vf yvxr fvyire va gur zvar'

function decodedCaesar(message, offset) {
  let decoded = [];
  var messageArray = message.split("");
  let plain = "abcdefghijklmnopqrstuvwxyz".split("");
  for (let j = 0; j < messageArray.length; j++) {
    if (messageArray[j] == " ") {
      decoded.push(messageArray[j]);
    }
    for (let i = 0; i < plain.length; i++) {
      if (
        messageArray[j].toLowerCase() == plain[i] &&
        i < plain.length - offset
      ) {
        decoded.push(plain[i + offset]);
      } else if (
        messageArray[j].toLowerCase() == plain[i] &&
        i >= plain.length - offset
      ) {
        decoded.push(plain[i - plain.length + offset]);
      }
      if (messageArray[j] == plain[i].toUpperCase()) {
        decoded[j] = decoded[j].toUpperCase();
      }
    }
  }
  return decoded.join("");
}

console.log(
  decodedCaesar("Genius without education is like silver in the mine", 18)
);

// Caesar Cipher 2
// Write a function decipher which is given a string, an offset, and returns the original message.

// decipher('Travhf jvgubhg rqhpngvba vf yvxr fvyire va gur zvar', offset)
// 'Genius without education is like silver in the mine'

function decodedCaesar(message, offset) {
  let decoded = [];
  var messageArray = message.split("");
  let plain = "abcdefghijklmnopqrstuvwxyz".split("");
  for (let j = 0; j < messageArray.length; j++) {
    if (messageArray[j] == " ") {
      decoded.push(messageArray[j]);
    }
    for (let i = 0; i < plain.length; i++) {
      if (messageArray[j].toLowerCase() == plain[i] && i < offset) {
        decoded.push(plain[i + plain.length - offset]);
      } else if (messageArray[j].toLowerCase() == plain[i] && i >= offset) {
        decoded.push(plain[i - offset]);
      }
      if (messageArray[j] == plain[i].toUpperCase()) {
        decoded[j] = decoded[j].toUpperCase();
      }
    }
  }
  return decoded.join("");
}

console.log(
  decodedCaesar("Ywfamk oalzgml wvmuslagf ak dacw kadnwj af lzw eafw", 18)
);

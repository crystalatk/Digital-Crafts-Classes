// Madlib
// Write a madlib function, which is given a name and a subject. It will return(not print) a new string: (name)'s favorite subject in school is (subject).

// madlib('Anushka', 'art');
// 'Anushka's favorite subject in school is art.'

function madLib(name, subject) {
  return `${name}'s favorite subject in school is ${subject}`;
}

console.log(madLib("Eddie", "math"));

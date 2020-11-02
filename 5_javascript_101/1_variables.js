// var do NOT use!!!
  var a;//declare before assigning
  a = 10;//assigning a declared variable
  var b = 10; //declaring and assigning
  b = 23; //re-assign variable
  /* var allows you to re-declare a variable inside of a function. This can and will lead to bugs and should no longer be used */

//   let
  let = a;
  let a = "Something" //ending simi-colon not required...
  a = 1
  /* let does not allow you to redeclare inside of a function. It should be used in place of var*/

//   const you can not change a value!
// also, since it can't be changed, it can't be declared without a value
  const a = 'someintin'
  a = 'something esle'//error cannot re-assign const.

  // Conventions: This is lower case, then upper case to divide words. This is the way it is expected to be written
  let camelCaseWin = 'Camel Case for the win'

  // Extras
  //declare multiple
  let a,b,c
  a = 1;
  b = 2;
  c = 3;
  //declaring and assigning multiple
  let e,f=10,g=12
  //e is undefined f is 10 g is 12
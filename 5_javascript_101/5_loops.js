// While Loops

  let i = 1;

  while(i < 10){
      console.log(i)
      i++
  }
  console.log(i)


  while(i > 0){
      console.log(i)
//you could do anything here
      i--
  }


//   //Infinate loops in the browser will cause the world to end. 
//   //Friends don't let friends infinate loop in the browser
// While statements are not used very often in js, least preferred way....

// //   for loops

//   //initial value; condition; incrimenter 
let num = 10  
for(let i = 0; i < num; i++){
      console.log(i)
  }

//   //optional leave out initial value: not as common!
  let i = 1
  for(; i<20; i++){
      console.log(i)
  }

// //   break

  let i = 0;
  while(i < 10){
      if(i > 5) break;//breaks the loop (this style is considered more elegant)
      console.log(i)
      i++
  }
//   //leaving out the condition ..infintate loop
//   for(let i = 0;;i++){
//       if(i > 10) {
//           break;
//       }
//       console.log(i)
//   }

// //   continue: while break takes you out of the loop, continue just takes you right to the next iteration...

  for(let i = 0;i<20;i++){
      if(!(i % 2)) continue; //zero is a falsey statement. So if not falsey is true and will take you to continue
      console.log(i)
  }

  for(let i = 0;i<20;i++){
    if(i % 2 == 0) continue;
    console.log(i)
}



//   //infinite loop warning!
//   let i = 0;
//   while(i < 10){
//       if(i % 2 == 0) continue;//why infinite loop?
//       console.log(i)
//       i++
//   }


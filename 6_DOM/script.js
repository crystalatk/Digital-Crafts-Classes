// //Exercise from lesson 5
// let main = document.querySelector("main");
// let myList = [
//   {
//     url: "http://google.com",
//     id: "google-link",
//     text: "go to Google!",
//   },
//   {
//     url: "http://facebook.com",
//     id: "facebook-link",
//     text: "go to Facebook",
//   },
// ];

// let ul = document.createElement("ul");
// main.append(ul);

// myList.forEach(function (item) {
//   let a = document.createElement("a");
//   a.href = item.url;
//   a.innerText = item.text;
//   let l = document.createElement("li");
//   l.append(a);
//   ul.append(l);
// });
// myArray = ["Pizza", "tacos", "burritos"];
// let header = document.querySelector("h1");
// let l = document.querySelectorAll("li");
// console.log(l);
// header.innerText = "This is the header!";
// l.forEach((element, idx) => {
//   console.log(element);
//   element.innerText = myArray[idx];
// });
// let paragraph = document.querySelector("p");
// paragraph.innerText =
//   "This is a paragraph. It is really fun. I hope lots of people read it. Women belong in all places where decisions are being made. Not fragile like a flower, fragile like a bomb.";

// console.log("Im here");

// let footer = document.querySelector("footer");
// console.log(footer);
// footer.classList.add("highlighted");

// let main = document.querySelector("#main-idea");
// let pets = document.querySelectorAll(".pet-name");
// let footie = document.querySelector("footer");

// let button = document.querySelector(".btn");

// button.onclick = function (event) {
//   console.log("happened");
//   button.style.background = "#329bdb";
// };

// let title = document.querySelectorAll(".title");

let num = 0;

let button = document.querySelector("h1");
button.classList.add("btn");

const func1 = function () {
  num++;
  if (num == 10) {
    button.removeEventListener("click", func1);
    button.style.background = "red";
  }
  button.innerHTML = num;
};

button.addEventListener("click", func1);

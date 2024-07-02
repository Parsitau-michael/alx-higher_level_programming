#!/usr/bin/node

const myArr = process.argv.slice(2).map(Number);

if (myArr.length <= 1) {
  console.log(0);
} else {
  myArr.sort((a, b) => b - a);
  console.log(myArr[1]);
}

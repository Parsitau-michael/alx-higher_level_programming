#!/usr/bin/node

// function to compute the factorial recursively
function factorial (a) {
  if (a <= 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

// parse cmd args and cast it as an Int
const num = parseInt(process.argv[2]);

// Compute the factorial, treating NaN as 1
const res = isNaN(num) ? 1 : factorial(num);

// printing the output
console.log(res);

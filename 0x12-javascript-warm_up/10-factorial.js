#!/usr/bin/node
// computes and prints a factorial

function factorial (number) {
  if (number === 0 || number === 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}
// console.log(Number(process.argv[2]));
if (process.argv.length === 2) {
  console.log(1);
} else {
  console.log(factorial(Number(process.argv[2])));
}

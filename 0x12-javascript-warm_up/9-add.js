#!/usr/bin/node
// prints the addition of 2 integers

function add (a, b) {
  console.log(Number(a) + Number(b));
}

add(process.argv[2], process.argv[3]);

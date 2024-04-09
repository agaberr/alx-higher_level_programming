#!/usr/bin/node
// prints a square

if (process.argv.length === 2 || !Number(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = Number(process.argv[2]);
  let X = '';
  for (let i = 0; i < size; i++) {
    X += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(X);
  }
}

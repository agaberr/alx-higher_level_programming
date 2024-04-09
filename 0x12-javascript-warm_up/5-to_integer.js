#!/usr/bin/node
// prints My number: <first argument converted in integer> if the first argument can be converted to an integer

if (process.argv.length === 2) {
  console.log('Not a number');
} else {
  // TODO: fix float
  if (Number(process.argv[2])) {
    console.log('My number: ' + Number(process.argv[2]));
  } else {
    console.log('Not a number');
  }
}

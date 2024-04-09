#!/usr/bin/node
// prints second largest number in arguments

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const sorted_list = process.argv.sort();
  console.log(sorted_list.reverse()[2]);
}

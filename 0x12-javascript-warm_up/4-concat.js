#!/usr/bin/node
/*
 * Script that prints two arguments passed to it,
 * in the following format: “ is ”.
*/

let len = 0;

// Getting the length of argv
process.argv.forEach((val, index) => {
  len += 1;
});

if (len === 2) {
  console.log('undefined is undefined');
} else if (len === 3) {
  console.log(process.argv[2] + ' is undefined');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}

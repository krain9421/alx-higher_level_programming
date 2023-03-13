#!/usr/bin/node
/*
 * Script that prints the first argument passed to it.
 * If no arguments are passed to the script, print “No argument”
*/

let len = 0;
const msg1 = 'No argument';

// Getting the length of argv
process.argv.forEach((val, index) => {
  len += 1;
});

if (len === 2) {
  console.log(msg1);
} else {
  console.log(process.argv[2]);
}

#!/usr/bin/node
/*
 * Script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer:
 * If the argument can’t be converted to an integer, print “Not a number”
*/

let len = 0;
const msg1 = 'Not a number';
const msg2 = 'My number: ';
let num = 0;

// Getting the length of argv
process.argv.forEach((val, index) => {
  len += 1;
});

if (len === 2) {
  console.log(msg1);
} else {
  num = parseInt(process.argv[2]);
  if (!num) {
    console.log(msg1);
  } else {
    console.log(msg2 + num);
  }
}

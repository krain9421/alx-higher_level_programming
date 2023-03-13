#!/usr/bin/node

const len = process.argv.length;
const msg1 = 'No argument';
const msg2 = 'Argument found';
const msg3 = 'Arguments found';

// Checking the arguments
if (len === 2) {
  console.log(msg1);
} else if (len === 3) {
  console.log(msg2);
} else {
  console.log(msg3);
}

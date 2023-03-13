#!/usr/bin/node
/*
 * Script that prints a square
 *
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer,
 * print “Missing size"
*/

const msg1 = 'Missing number of occurences';
const X = 'X';
let txt = '';
let i = 0; // Index for looping
let j = 0; // Index for looping

// The Loop
if (!parseInt(process.argv[2])) {
  console.log(msg1);
} else {
  for (i; i < process.argv[2]; i++) {
    for (j; j < process.argv[2]; j++) {
      txt += 'X';
    }
    console.log(txt);
  }
}

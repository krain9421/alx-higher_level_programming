#!/usr/bin/node
/*
 * Script that prints x times "C is fun"
 *
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer,
 * print “Missing number of occurences"
*/

const msg1 = 'Missing number of occurences';
const msg2 = 'C is fun';
const len = process.argv.length;
let i = 0; // Index for looping

// The Loop
if (!parseInt(process.argv[2])) {
  console.log(msg1);
} else {
  for (i; i < process.argv[2]; i++) {
    console.log(msg2);
  }
}

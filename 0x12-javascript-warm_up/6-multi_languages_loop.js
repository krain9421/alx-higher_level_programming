#!/usr/bin/node
/*
 * Script that prints 3 lines by using
 * an array of strings and a loop
 * If no arguments are passed to the script, print “No argument”
*/

const msg1 = 'C is fun';
const msg2 = 'Python is cool';
const msg3 = 'JavaScript is amazing';
const lines = [msg1, msg2, msg3];

// Printing out the lines in the array
lines.forEach((val) => {
  console.log(val);
});

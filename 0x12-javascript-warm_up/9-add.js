#!/usr/bin/node
/*
 * Script that prints the addition of 2 integers
 *
 * The first argument is the first integer
 * The second argument is the second integer
*/

let num1 = 0;
let num2 = 0;

function add (a, b) {
  return a + b;
}

// Feeding the command arguments to the function
num1 = parseInt(process.argv[2]);
num2 = parseInt(process.argv[3]);
console.log(add(num1, num2));

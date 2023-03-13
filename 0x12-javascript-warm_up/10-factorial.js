#!/usr/bin/node
/*
 * Script that computes and prints a factorial
 *
 * The first argument is integer used for computing the factorial
 * Factorial of NaN is 1
*/

function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

// Feeding the command arguments to the function
if (!parseInt(process.argv[2])) {
  console.log('1');
} else {
  console.log(factorial(process.argv[2]));
}

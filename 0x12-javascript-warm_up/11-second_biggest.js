#!/usr/bin/node
/*
 * Script that searches the second biggest integer in the list of arguments
 *
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
*/

const len = process.argv.length;
let len2 = 0;
let argvNew = [];
let i = 0; // Integer for indexing

// Checking the command arguments
if (len >= 2 && len <= 3) {
  console.log('0');
} else {
  len2 = process.argv.length;
  argvNew = process.argv.slice(2, len2);
  argvNew.sort((a, b) => a - b);
  len2 = argvNew.length;
  
  for (i = len2 - 2; i >= 0; i--) {
    if (argvNew[i] != argvNew[len - 1]) {
      console.log(argvNew[i]);
      break;
    }
  }
  console.log(argvNew[len2 - 2]);
}

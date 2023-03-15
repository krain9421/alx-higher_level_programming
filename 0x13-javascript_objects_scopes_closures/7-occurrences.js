#!/usr/bin/node
/*
 * Function that returns the number of occurences in a list.
*/
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((val) => {
    if (val === searchElement) {
      count++;
    }
  });
  return count;
};

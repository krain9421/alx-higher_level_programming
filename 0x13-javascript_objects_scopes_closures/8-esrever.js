#!/usr/bin/node
/*
 * Function that returns the reversed version of a list.
*/
exports.esrever = function (list) {
  const reversed = [];
  const len = list.length;

  for (let i = len - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};

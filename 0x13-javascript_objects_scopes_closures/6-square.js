#!/usr/bin/node
/*
 * Class Square that defines a square and inherits from
 * Square of 5-square.js
 * Method charPrint(c) prints the rectangel using the
 * character c
 * If c is undefined, use the character X
*/

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let txt = '';
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height; j++) {
        txt += c;
      }
      console.log(txt);
      txt = '';
    }
  }
};

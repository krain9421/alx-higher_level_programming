#!/usr/bin/node
/*
 * Class Square that defines a square and inherits from
 * Rectangle of 4-rectangle.js
 * The constructor takes 1 argument of size
*/

module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};

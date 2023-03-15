#!/usr/bin/node
/*
 * Class Rectangle that defines a rectangle
 * The constructor takes 2 arguments w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * If w or h is equal to 0 or not a positive integer, create
 * an empty object
 * Method print() prints the rectangel using the xter X
 * Method rotate() exchanges the width and height of the rectangle
 * Method double() multiplies the width and height by 2
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let txt = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        txt += 'X';
      }
      console.log(txt);
      txt = '';
    }
  }

  rotate () {
    let temp = 0;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};

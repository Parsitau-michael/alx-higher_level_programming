#!/usr/bin/node

// Class Rectangle
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // instance method that prints the rectangle using X
  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  // Instance method that exchanges the width and
  // the height of the rectangle.
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Instance method that multiples the width and
  // the height of the rectangle by 2.
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

// Exporting the class
module.exports = Rectangle;

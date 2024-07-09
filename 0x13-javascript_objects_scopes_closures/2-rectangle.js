#!/usr/bin/node

// Class Rectangle
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

// Exporting the class
module.exports = Rectangle;

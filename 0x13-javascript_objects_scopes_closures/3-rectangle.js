#!/usr/bin/node

class Rectangle {
  constructor (wi, hi) {
    if (wi > 0 && hi > 0) {
      this.width = wi;
      this.height = hi;
    }
  }

  print () {
    for (let k = 0; k < this.height; k++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;

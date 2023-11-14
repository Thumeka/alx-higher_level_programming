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

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;

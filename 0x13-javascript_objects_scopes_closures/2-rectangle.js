#!/usr/bin/node

class Rectangle {
  constructor (wi, hi) {
    if (wi > 0 && hi > 0) {
      this.width = wi;
      this.height = hi;
    }
  }
}
module.exports = Rectangle;

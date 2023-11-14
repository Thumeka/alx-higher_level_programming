#!/usr/bin/node

class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c !== undefined) {
      for (let k = 0; k < this.height; k++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;

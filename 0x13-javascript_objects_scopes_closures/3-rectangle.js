#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let count = 0;
    while (count < this.height) {
      console.log('X'.repeat(this.width));
      count++;
    }
  }
};

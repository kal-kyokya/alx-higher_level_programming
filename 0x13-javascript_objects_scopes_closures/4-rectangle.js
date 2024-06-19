#!/usr/bin/node
module.exports = class Rectngle {
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

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};

#!/usr/bin/node
const Sqr = require('./5-square');

module.exports = class Square extends Sqr {
  charPrint (myChar) {
    if (myChar === undefined) {
      this.print();
    } else {
      let count = 0;
      while (count < this.height) {
        console.log(myChar.repeat(this.width));
        count++;
      }
    }
  }
};

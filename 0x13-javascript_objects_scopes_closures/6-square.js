#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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

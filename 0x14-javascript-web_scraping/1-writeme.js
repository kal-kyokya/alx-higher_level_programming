#!/usr/bin/node
// Script that writes a string to a file
const fileSystem = require('fs');

fileSystem.writeFile(process.argv[2], process.argv[3], 'UTF-8', (err) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
});

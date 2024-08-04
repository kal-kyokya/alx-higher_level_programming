#!/usr/bin/node
// Reads the content of a file and send it to standard output
const fileSystem = require('fs');

fileSystem.readFile(process.argv[2], 'UTF-8', (err, fileContent) => {
  if (err) {
    console.log('Error occured during reading of file');
    process.exit(1);
  }
  console.log(fileContent);
});

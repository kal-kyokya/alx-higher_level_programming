#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let count = 0;
  while (count < parseInt(process.argv[2])) {
    console.log('X'.repeat(parseInt(process.argv[2])));
    count++;
  }
}

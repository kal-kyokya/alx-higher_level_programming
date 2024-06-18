#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let count = 0;
  while (count < parseInt(process.argv[2]))
  {
    console.log('C is fun');
    count++;
  }
}

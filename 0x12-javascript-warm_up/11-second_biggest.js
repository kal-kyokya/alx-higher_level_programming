#!/usr/bin/node
const [, , ...args] = process.argv;

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const numbers = args.map(arg => parseInt(arg, 10));
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}

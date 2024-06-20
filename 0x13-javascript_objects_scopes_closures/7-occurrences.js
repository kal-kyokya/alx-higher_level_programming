#!/usr/bin/node
exports.nbOccurences = function (list, value) {
  let count = 0;
  let occurences = 0;
  while (count < list.length) {
    if (list[count] === value) {
      occurences++;
    }
    count++;
  }

  return (occurences);
};

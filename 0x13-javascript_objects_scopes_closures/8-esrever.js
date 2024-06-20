#!/usr/bin/node
exports.esrever = function esrever (list) {
    return (list.sort((num1, num2) => num2 - num1));
};

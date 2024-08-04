#!/usr/bin/node
// Computes the number of task completed by user id
const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const tasks = JSON.parse(body);
  const set = new Set();

  tasks.forEach(task => {
    if (!set.has(task.userId)) {
      set.add(task.userId);
    }
  });

  const users = [...set];

  const obj = {};
  users.forEach(id => {
    obj[id] = 0;
  });

  tasks.forEach(task => {
    if (task.completed) {
      const userId = task.userId;
      obj[userId]++;
    }
  });
});

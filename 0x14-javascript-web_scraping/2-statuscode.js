#!/usr/bin/node
/**
   Displays the status code of a 'GET' request
   The status code must be printed like this:
       code: <status code>
**/
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
      console.error('code:', error);
    process.exit(1);
  }
  console.log('code:', response && response.statusCode);
});

#!/usr/bin/node
// Prints title of a Star Wars movies based on the episode number
const request = require('request');

const episodeID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const resource = url + episodeID;
request(resource, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  const parsedBody = JSON.parse(body);
  console.log(parsedBody.title);
});

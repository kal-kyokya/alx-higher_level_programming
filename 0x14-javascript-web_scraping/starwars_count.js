#!/usr/bin/node
// Computes number of movies containing a pattern
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, (error, response, body) => {
  if (error) {
    console.error('Error: ', error);
    process.exit(1);
  }
  const parsedBody = JSON.parse(body);
  const results = parsedBody.results;

  let count = 0;
  results.forEach((movie) => {
    const regex = /^(?:(?!18).)*$/;
    const characters = movie.characters;

    characters.forEach((actor) => {
      if (!regex.test(actor)) {
        count++;
      }
    });
  });
  console.log(count);
});

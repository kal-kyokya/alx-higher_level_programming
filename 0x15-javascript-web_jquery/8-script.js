#!/usr/bin/env node
// Fetches and lists title for all movies from an API

// Get all movies (API response)
$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (response) {
      // Continuously 'Extract movie titles' and 'add to unordered list'
      const films = response.results;
      films.forEach(function (movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    },
    error: function () {
      console.log('Errare humanum est, (sed) perseverare diabolicum');
    }
  });
});

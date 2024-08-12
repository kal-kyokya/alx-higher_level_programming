#!/usr/bin/env node
// Gets data from an API and parses the name out before display

// Send request
$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (response) {
      // Retrieve name attribute from response
      // Pass name inside div of ID character
      $('#character').text(response.name);
    },
    error: function () {
      console.log('You done Fvcked up, Nikkah');
    }
  });
});

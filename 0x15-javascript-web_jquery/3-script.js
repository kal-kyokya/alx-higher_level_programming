#!/usr/bin/env node
// Adds a class to the 'header' element

try {
  $('document').ready(function () {
    $('header').addClass('red');
  });
} catch (e) {
  console.log(e);
}

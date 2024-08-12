#!/usr/bin/env node
// Upon click on 'div', updates the text color of the 'header' element

try {
  $('document').ready(function () {
    $('#red_header').click(function () {
      $('header').css('color', '#FF0000');
    });
  });
} catch (e) {
  console.log(e);
}

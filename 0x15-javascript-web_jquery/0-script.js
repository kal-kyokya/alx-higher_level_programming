#!/usr/bin/env node
// Updates the text color of the 'header' element
try {
    var header = document.querySelector('header');
    header.style.color = '#FF0000';
} catch (e) {
    console.log(e);
}

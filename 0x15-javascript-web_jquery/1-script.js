#!/usr/bin/env node
// Updates the text color of the 'header' element
try {
    $('document').ready(function() {
	$('header').css('color', '#FF0000');
    })
} catch (e) {
    console.log(e);
}


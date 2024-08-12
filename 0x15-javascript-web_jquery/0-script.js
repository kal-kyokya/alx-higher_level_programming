#!/usr/bin/env node
// Using 'querySelector', updates the text color of the 'header' element
try {
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
} catch (e) {
  console.log(e);
}

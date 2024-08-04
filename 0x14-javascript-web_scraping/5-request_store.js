#!/usr/bin/node
// Request api resource and store it in file
const request = require('request');
const fileSystem = require('fs');

url = process.argv[2];
filename = process.argv[3];

request(url, (error, response, body) => {
    if (error) {
	console.log(error);
	process.exit(1);
    }
    fileSystem.writeFile(filename, body, (err) => {
	if (err) {
	    console.log(err);
	    process.exit(1);
	}
    });
});

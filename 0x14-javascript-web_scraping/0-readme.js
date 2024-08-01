#!/usr/bin/node

let fs = require('fs');

let read_string = fs.readFile(process.argv[2], 'utf8', function (err, data) {
	if (err)
		return console.error(err);
	console.log(data);
});

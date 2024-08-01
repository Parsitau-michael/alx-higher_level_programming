#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request({ url: url, json: true }, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const movies = body.results;
  let count = 0;

  for (const movie of movies) {
    if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});

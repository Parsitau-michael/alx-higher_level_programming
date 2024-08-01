#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request({ url: url, json: true }, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(body.title);
});

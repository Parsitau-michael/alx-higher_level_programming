#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request({ url: url, json: true }, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(body.title);
});

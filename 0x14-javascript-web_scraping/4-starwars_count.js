#!/usr/bin/node
// This JS script prints the number of movies where
// the character “Wedge Antilles” is present.

const req = require('request');
const url = process.argv[2];
const log = (arg) => console.log(arg);
let counter = 0;

req(url, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  const data = JSON.parse(body);

  data.results.forEach((movie) => {
    movie.characters.forEach((char) => {
      if (char.includes(18)) {
        counter += 1;
      }
    });
  });

  log(counter);
});

#!/usr/bin/node
// This JS script get the contents of a webpage and stores it in a file.

const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

req.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
  });
});

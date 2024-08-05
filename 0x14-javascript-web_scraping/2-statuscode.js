#!/usr/bin/node
// This JS script displays the status code of a GET request.

const req = require('request');
const url = process.argv[2];
const log = (arg) => console.log(arg);

req.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  log(`code: ${res.statusCode}`);
});

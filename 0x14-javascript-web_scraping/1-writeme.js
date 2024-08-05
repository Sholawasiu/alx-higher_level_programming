#!/usr/bin/node
// This JS script writes a string to a file.

const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];

fs.writeFile(file, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});

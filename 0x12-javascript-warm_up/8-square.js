#!/usr/bin/node
const log = (arg) => console.log(arg);
const size = (process.argv[2]);
const char = 'X';

if (isNaN(size)) {
  log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let j = 0; j < size; j++) {
      line += `${char}`;
    }
    log(`${line}`);
  }
}

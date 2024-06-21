#!/usr/bin/node
const log = (arg) => console.log(arg);
const x = parseInt(process.argv[2]);
const str = 'C is fun';

if (isNaN(x)) {
  log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    log(`${str}`);
  }
}

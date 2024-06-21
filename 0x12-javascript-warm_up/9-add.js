#!/usr/bin/node
const log = (arg) => console.log(arg);
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

log(a === 'undefined' || b === 'undefined' ? NaN : add(a, b));

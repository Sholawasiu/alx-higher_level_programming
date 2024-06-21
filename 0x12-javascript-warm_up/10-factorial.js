#!/usr/bin/node
const log = (arg) => console.log(arg);
const arg = parseInt(process.argv[2]);

function factorial (num) {
  if (num < 2) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

log(isNaN(arg) ? 1 : factorial(arg));

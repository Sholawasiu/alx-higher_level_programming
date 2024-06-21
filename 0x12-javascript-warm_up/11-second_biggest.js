#!/usr/bin/node
const log = (arg) => console.log(arg);
const args = process.argv;

function secondBiggest (arr) {
  return arr[arr.length - 2];
}

function compareFn (a, b) {
  return a - b;
}

if (args.length <= 3) {
  log(0);
} else {
  args.sort(compareFn);
  log(secondBiggest(args));
}

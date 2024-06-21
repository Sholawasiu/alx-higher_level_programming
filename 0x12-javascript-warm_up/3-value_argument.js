#!/usr/bin/node
const arg = process.argv[2];
const log = (arg) => console.log(arg);
log(typeof arg === 'undefined' ? 'No argument' : arg);

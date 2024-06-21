#!/usr/bin/node
const args = process.argv;
const log = (arg) => console.log(arg);
const str = 'is';

log(`${args[2]} ${str} ${args[3]}`);

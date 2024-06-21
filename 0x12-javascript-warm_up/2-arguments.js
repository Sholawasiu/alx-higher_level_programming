#!/usr/bin/node
const args = process.argv.length;
const log = (arg) => console.log(arg);
const str = 'Argument';

if (args === 2) {
  log('No argument');
} else {
  args === 3 ? log(`${str} found`) : log(`${str}s found`);
}

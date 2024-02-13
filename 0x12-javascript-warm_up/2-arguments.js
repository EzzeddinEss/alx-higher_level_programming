#!/usr/bin/node
const arg1 = 'No argument';
const arg2 = 'Argument found';
const arg3 = 'Arguments found';
const argsCount = process.argv.length - 2;

if (argsCount === 0) {
  console.log(arg1);
} else if (argsCount === 1) {
  console.log(arg2);
} else {
  console.log(arg3);
}

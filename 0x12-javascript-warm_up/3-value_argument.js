#!/usr/bin/node
const arg1 = 'No argument';
const argsCount = process.argv.slice(2);

if (argsCount[0]) {
  console.log(argsCount[0]);
} else {
  console.log(arg1);
}

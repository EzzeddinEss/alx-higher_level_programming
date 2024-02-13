#!/usr/bin/node
const argsCount = process.argv.slice(2);

if (argsCount.length >= 2) {
  console.log(argsCount[0] + ' is ' + argsCount[1]);
} else if (argsCount.length === 1) {
  console.log(argsCount[0] + ' is ' + 'undefined');
} else {
  console.log('undefined' + ' is ' + 'undefined');
}

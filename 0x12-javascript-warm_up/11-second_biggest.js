#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const myArgs = process.argv.slice(2);
  const secondBig = myArgs.sort((a, b) => b - a)[1];
  console.log(secondBig);
}

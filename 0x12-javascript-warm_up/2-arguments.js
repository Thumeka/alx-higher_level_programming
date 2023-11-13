#!/usr/bin/node
const myArgs = process.argv.length;
console.log(myArgs === 2 ? 'No argument' : myArgs === 3 ? 'Argument found' : 'Arguments found');

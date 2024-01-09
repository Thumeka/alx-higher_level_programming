#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (er, data) => {
  if (er) {
    console.error(er);
    return;
  }
  console.log(data);
});

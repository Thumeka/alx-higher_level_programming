#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], function (er) {
  if (er) return console.log(er);
});

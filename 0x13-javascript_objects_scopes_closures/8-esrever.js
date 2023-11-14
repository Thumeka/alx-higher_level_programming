#!/usr/bin/node
exports.esrever = function (list) {
  const rev = list.map(list.pop, [...list]);
  return rev;
};

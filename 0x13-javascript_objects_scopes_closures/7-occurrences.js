#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const countOccurences = list.reduce((nb, val) => (val === searchElement ? nb + 1 : nb), 0);
  return countOccurences;
};

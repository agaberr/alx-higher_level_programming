#!/usr/bin/node

exports.callMeMoby = function (x, myfunction) {
  for (let i = 0; i < x; i++) {
    myfunction();
  }
};

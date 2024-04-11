#!/usr/bin/node

function callMeMoby (x, myfunction) {
  for (let i = 0; i < x; i++) {
    myfunction();
  }
}

module.exports = callMeMoby;

#!/usr/bin/node
const request = require('request');
const fs = require('fs');

url = `${process.argv[2]}`;
txtFile = `${process.argv[3]}`;

request(url).pipe(fs.createWriteStream(txtFile));

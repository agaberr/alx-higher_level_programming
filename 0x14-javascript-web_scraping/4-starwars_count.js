#!/usr/bin/node
const request = require('request');

url = process.argv[2];

let filmsCount = 0;

request(url, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {

        for (let movie of JSON.parse(body).results) {
            for (let character in movie.characters) {
                // console.log(character);
                if (character === '18') {
                    filmsCount++;
                }
        }
        
    }
    console.log(filmsCount);
}
});

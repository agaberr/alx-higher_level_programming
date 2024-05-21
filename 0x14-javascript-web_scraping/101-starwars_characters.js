#!/usr/bin/node
const request = require('request');

url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`



request(url, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {

        for (let characterUrl of JSON.parse(body).characters) {
                request(characterUrl, (error, response, body) => {
                    
                    if (error) {
                        console.log(error);
                    } else {
                    console.log(JSON.parse(body).name);
                    }
                
                }
        );
        }
        
    }

});

#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const wedgeAntillesId = '18';

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let filmsCount = 0;

    films.forEach(film => {
      film.characters.forEach(characterUrl => {
        if (characterUrl.includes(`/people/${wedgeAntillesId}/`)) {
          filmsCount++;
        }
      });
    });

    console.log(filmsCount);
  }
});

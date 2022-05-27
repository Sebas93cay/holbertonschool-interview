#!/usr/bin/node

const request = require('request');

const args = process.argv.slice(2);

const main = async () => {
  if (args.length === 0) {
    console.log('Movie id not inserted');
    return;
  }
  const id = Number(args[0]);
  if (!Number.isInteger(id)) {
    console.log('Invalid Id');
    return;
  }

  const movieInfo = await new Promise((resolve, reject) => {
    request('https://swapi-api.hbtn.io/api/films/' + id, (err, res, body) => {
      if (err) {
        console.error('error:\n', err); // Print the error if one occurred
        resolve(null);
      }
      resolve(JSON.parse(body));
    });
  });

  if (!movieInfo) return;

  const characters = movieInfo.characters;

  const namesPromises = [];
  characters.forEach((characterUrl) => {
    namesPromises.push(
      new Promise((resolve) => {
        request(characterUrl, (err, res, body) => {
          if (err) {
            console.error(`error in character for url ${characterUrl}\n`, err);
            resolve(null);
          }
          resolve(JSON.parse(body).name);
        });
      }),
    );
  });

  Promise.all(namesPromises).then((names) => {
    names.forEach((name) => console.log(name));
  });
};

main();

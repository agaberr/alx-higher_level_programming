#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

tasks = {};

request(url, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        for (let task of JSON.parse(body))
            {
                if (task.completed === true)
                    {
                        if (tasks[task.userId] === undefined)
                            {
                                tasks[task.userId] = 1;
                            }
                        else
                            {
                                tasks[task.userId]++;
                            }
                    }
            }
        console.log(tasks);
    }
});
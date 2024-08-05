#!/usr/bin/node
// This JS script computes the number of tasks completed by user id.

const req = require('request');
const url = process.argv[2];
const completedTasks = {};
const log = (arg) => console.log(arg);

req.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  const data = JSON.parse(body);

  data.forEach((task) => {
    if (task.completed) {
      if (!completedTasks[task.userId]) {
        completedTasks[task.userId] = 1;
      } else {
        completedTasks[task.userId] += 1;
      }
    }
  });

  log(completedTasks);
});

#!/usr/bin/node

const request = require('request');

request(process.argv[2], { json: true }, function (error, response, body) {
  if (error) {
    console.error(error);
  }

  const taskCount = {};
  body.forEach(task => {
    if (task.completed) {
      if (!taskCount[task.userId]) {
        taskCount[task.userId] = 0;
      }
      taskCount[task.userId]++;
    }
  });

  console.log(JSON.stringify(taskCount, null, 2));
});

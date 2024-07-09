#!/usr/bin/node
const noOcc = process.argv[2];
if (!parseInt(noOcc)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < parseInt(noOcc); i++) {
  console.log('C is fun');
}

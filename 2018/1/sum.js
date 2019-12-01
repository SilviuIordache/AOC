
const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: fs.createReadStream('./input.txt'),
  output: process.stdout,
  terminal: false
});

let sum = 0;
let arr = [ ];

arr.push(sum);

rl.on('line', (line) => {
  sum += +line;
});

rl.on('close', () => {
  console.log(sum);
})

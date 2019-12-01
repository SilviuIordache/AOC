
const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: fs.createReadStream('./input.txt'),
  output: process.stdout,
  terminal: false
});


let calculateFuel = function(value) {
  return Math.floor(value / 3) - 2
}

let fuelSum = 0;

rl.on('line', (line) => {
  fuelSum += calculateFuel(line);
  //console.log(fuelSum);
});

rl.on('close', () => {
  console.log(fuelSum);
})



const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: fs.createReadStream('./input.txt'),
  output: process.stdout,
  terminal: false
});


let calculateFuel = function(value) {
  let fuel = Math.floor(value / 3) - 2;
  if (fuel < 0) {
    return 0;
  } else {
    return fuel + calculateFuel(fuel);
  }
}

let fuelSum = 0;

rl.on('line', (line) => {
  fuelSum += calculateFuel(line);
});

rl.on('close', () => {
  console.log(fuelSum);
})

const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: fs.createReadStream('./input.txt'),
  output: process.stdout,
  terminal: false
});

let arr = [ ];

rl.on('line', (line) => {
  arr.push(+line);
});

rl.on('close', () => {
  findFirstDuplicate(arr);
})

let findFirstDuplicate = function(arr) {
  let sumArray = [];
  let duplicateSumFound = false;
  let duplicateSum;
  let currentSum = 0;
  let firstRun = true;

  
  while(duplicateSumFound === false) {
    for (let i = 0; i < arr.length; i++) {
      currentSum += arr[i];
  
      if(!firstRun && sumArray.includes(currentSum)) {
        console.log('found duplicate: ', currentSum);
        duplicateSumFound = true;
        duplicateSum = currentSum;
        return;
      } else {
        sumArray.push(currentSum);
      }
      if (firstRun) {
        firstRun = false
      }
    }
  }
  console.log('duplicateSum: ', duplicateSum);
}

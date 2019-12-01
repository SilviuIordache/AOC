
const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: fs.createReadStream('./input.txt'),
  output: process.stdout,
  terminal: false
});


let duoCount = 0;
let trioCount = 0


rl.on('line', (line) => {
  if (countOccurences(line).duo.state === true)
    duoCount++;
  if (countOccurences(line).trio.state === true)
    trioCount++;
});

rl.on('close', () => {
  console.log(duoCount * trioCount);
});

let countOccurences = function(code) {
  let duo  = { state: false, letter: '', backUpFound: false, backUp: '' }
  let trio = { state: false, letter: '' }
  let occurence = {};
  for (let i = 0; i < code.length; i++) {
    if (occurence[code[i]] > 0) {
      occurence[code[i]]++;
      if (occurence[code[i]] === 2) {
        if (duo.state === false) {
          duo.state = true;
          duo.letter = code[i];
        } else if (duo.backUpFound === false) {
          duo.backUp = code[i];
          duo.backUpFound = true;
        }
        //console.log('duo: ', duo);
      }
      if (occurence[code[i]] === 3) {
        if (duo.letter === code[i]) {
          if(duo.backUpFound) {
            duo.letter = duo.backUp;
            duo.backUp = '';
            duo.backUpFound = false;
          } else {
            duo.state = false;
            duo.letter = '';
          }
          trio.state = true;
          trio.letter = code[i];
          //console.log('trio: ', trio);
        } else {
          trio.state = true;
          trio.letter = code[i];
        }
      }
    } else {
      occurence[code[i]] = 1;
    }
  }
  return { duo, trio };
}

countOccurences('ababab');



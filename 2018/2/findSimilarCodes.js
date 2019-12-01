
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

const codesArr = [];

rl.on('line', (line) => {
  codesArr.push(line)
});

rl.on('close', () => {
  console.log(compareCodes(codesArr));
})

// find the 2 codes which differ by exactly 1 character


let similarCheck = function(code1, code2) {
  let commonPart = '';
  for (let i = 0; i < code1.length; i++) {
    if (code1[i] === code2[i]) {
      commonPart += code1[i];
      //console.log(commonPart);
    }
  }
  if (code1.length - commonPart.length === 1) {
    return commonPart;
  } else {
    return false;
  }
}


let compareCodes = function(codes) {
  for (let i = 0 ; i < codes.length; i++) {
    for (let j = 0 ; j < codes.length; j++) {
      if (similarCheck(codes[i], codes[j]) != false) {
        console.log('found similar')
        return similarCheck(codes[i], codes[j]);
      }
        
    }
  }
}

// let code1 = 'fghij';
// let code2 = 'fguij';
// console.log(similarCheck(code1, code2));


// find the unique portion of the code

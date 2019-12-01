
const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: fs.createReadStream('./input.txt'),
  output: process.stdout,
  terminal: false
});

const produceMaterial = function(length, height) {
  let matrix = [];
  for (let i = 0; i < height; i++) {
    let newLine = [];
    for (let j = 0; j < length; j++) {
      newLine.push('.');
    }
    matrix.push(newLine);
  }
  return matrix;
}

let getClaimValues = function(claim) {
  const claimNumber = claim.split('@')[0].trim().substr(1);

  let materialSizes = claim.split('@')[1].split(':')

  let margins = materialSizes[0].split(',');
  let lengths = materialSizes[1].split('x');

  let marginLeft = margins[0].trim();
  let marginTop = margins[1].trim();

  let width = lengths[0].trim();
  let height = lengths[1].trim();

  return {
    claimNumber,
    marginLeft: parseInt(marginLeft, 10),
    marginTop: parseInt(marginTop, 10),
    width: parseInt(width, 10),
    height: parseInt(height, 10)
  }
}

let markMaterial = function(material, claimValues) {
  let { claimNumber, marginLeft, marginTop, width, height} = claimValues;

  for (let i = marginTop ; i < (marginTop + height); i++) {
    for (let j = marginLeft; j < (marginLeft + width); j++) {
      if (material[i][j] === '.') {
        material[i][j] = claimNumber;
      } else {
        material[i][j] = 'X';
      }
    }
  }
}

let countCharacter = function(material, charToFind) {
  let overlappingMaterial = 0;
  for (let i = 0; i < material.length; i++) {
    let row = material[i];
    for (let j = 0; j < row.length; j++) {
      if (row[j] === charToFind) {
        overlappingMaterial++;
      }
    }
  }
  return overlappingMaterial;
}

let getUntouchedClaim = function(material, claims) {
  let claimSize = 0;
  for (let claim of claims) {
    claimSize = claim.width * claim.height;
    if (countCharacter(material, claim.claimNumber) === claimSize) {
      return claim.claimNumber;
    }
  }
}

let material = produceMaterial(1000, 1000);
let claims = [];
rl.on('line', (line) => {
  let claimValues = getClaimValues(line);
  claims.push(claimValues);
  markMaterial(material, claimValues);
});

rl.on('close', () => {
  console.log(countCharacter(material, 'X'));
  console.log(getUntouchedClaim(material, claims));
})


// let material = produceMaterial(11, 9);
// console.log( material);
// let claim = '#1 @ 3,2: 5x4';
// let claimValues = getClaimValues(claim);

// console.log(claimValues)
// markMaterial(material, claimValues);

// let material = produceMaterial(11, 9);
// let claims = ['#1 @ 1,3: 4x4','#2 @ 3,1: 4x4','#3 @ 5,5: 2x2'] ;
// for (let i = 0 ; i < claims.length; i++) {
//   let claimValues = getClaimValues(claims[i]);
//   markMaterial(material, claimValues);
// }
// console.log(material);
// console.log(countOverlapping(material));

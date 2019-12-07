const fs = require('fs');
const readline = require('readline');
var Combinatorics = require('js-combinatorics');

const rl = readline.createInterface({
  //input: fs.createReadStream('./input.txt'),
  input: fs.createReadStream('./2019/7/input.txt'),
  output: process.stdout,
  terminal: false
});

rl.on('line', function(line) {
  //getHighestSignal(line)
})


let calculator = function(code, phase, input = 5) {
  let arr = code.split(',').map(function(item) {
      return parseInt(item, 10);
  })

  let pos = 0;
  let param1;
  let param2;
  let phaseSet = false;

  while (arr[pos] != 99) {
    let currValue = arr[pos]
    let inst = getInstructionData(currValue);
    let { opcode, p1, p2} = inst;

    val1 = arr[pos + 1]
    val2 = arr[pos + 2]

    param1 = mval(p1, arr[pos + 1], arr);
    param2 = mval(p2, arr[pos + 2], arr);

    switch(opcode) {
      case 1:
        arr[arr[pos + 3]] = param1 + param2;
        pos += 4;  
        break;
      case 2:
        arr[arr[pos + 3]] = param1* param2;
        pos += 4;  
        break;
      case 3:
        if (phaseSet === false) {
          arr[arr[pos + 1]] = phase
          phaseSet = true;
        } else {
          arr[arr[pos + 1]] = input;
        }
        pos += 2;
        break;
      case 4:
        return param1
      case 5:
        pos = (param1 != 0) ? param2 : pos + 3
        break;
      case 6:
        pos = (param1 === 0) ? param2 : pos + 3
        break;
      case 7:
        arr[arr[pos + 3]] = (param1 < param2) ? 1 : 0;
        pos += 4; 
        break;
      case 8:
        arr[arr[pos + 3]] = (param1 === param2) ? 1 : 0;
        pos +=4;
      break;
      default:
        break;
    }
  }
}

let mval = function(mode, value, arr) {
  if (mode == 0) {
    return arr[value];
  } else {
    return value;
  }
}

let getInstructionData = function(number) {
  return {
    opcode: number % 100,
    p1: ((number - number % 100) / 100) % 10,
    p2: ((number - number % 1000) / 1000) % 10,
    p3: ((number - number % 10000) / 10000) % 10
  }
}

let getPermutations = function() {
  cmb = Combinatorics.permutation([5, 6, 7, 8, 9]);
  return cmb.toArray();
}


let amplifySignal= function (signal, module1Input, phaseSetting) {

  module1 = calculator(signal, phaseSetting[0], module1Input)
  module2 = calculator(signal, phaseSetting[1], module1)
  module3 = calculator(signal, phaseSetting[2], module2)
  module4 = calculator(signal, phaseSetting[3], module3)
  module5 = calculator(signal, phaseSetting[4], module4)

  return module5;
}

let getHighestSignal = function(signal) {
  let maxSignalPerm = []
  let maxSignal = -1;
  let phases = getPermutations();

  for (let i = 0 ; i < phases.length; i++) {
    let currPhase = phases[i];
    let val = amplifySignal(signal, 0, currPhase);

    while (val) {
      if(val > maxSignal) {
        maxSignal = val;
        maxSignalPerm = phases[i]
      }
      val = amplifySignal(signal, val, currPhase);
    }
    
  }
  
  console.log(maxSignal, maxSignalPerm);
}


let signal1 = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5';
let signal2 = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'

getHighestSignal(signal1)
//getHighestSignal(signal2)
// getHighestSignal(signal3)
const fs = require('fs');
const readline = require('readline');
var Combinatorics = require('js-combinatorics');

const rl = readline.createInterface({
  //input: fs.createReadStream('./input.txt'),
  input: fs.createReadStream('./2019/5/input.txt'),
  output: process.stdout,
  terminal: false
});

rl.on('line', function(line) {
  getHighestSignal(line)
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
  cmb = Combinatorics.permutation([0, 1, 2, 3, 4]);
  return cmb.toArray();
}


let amplifySignal= function (signal, phaseSetting) {

  module1 = calculator(signal, phaseSetting[0], 0)
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
    let val = amplifySignal(signal, phases[i]);
    if(val > maxSignal) {
      maxSignal = val;
      maxSignalPerm = phases[i]
    }
  }
  
  console.log(maxSignal, maxSignalPerm);
}


let signal1 = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0';
let signal2 = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0';
let signal3 = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0';


getHighestSignal(signal1)
getHighestSignal(signal2)
getHighestSignal(signal3)
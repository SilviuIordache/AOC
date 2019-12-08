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


let calculator = function(arr, phase, input, pos) {
  
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
        return {
          output: param1,
          pos,
          arr
        }
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

  let arr = signal.split(',').map(function(item) {
    return parseInt(item, 10);
  })

  modules = [0, 0, 0, 0, 0];
  let {output, pos, arr} = calculator(arr, phaseSetting[0], module1Input, 0)
  modules[0] = val;

  let i = 1;
  while (val != undefined) {
    if (i % 5 != 0) {
      let {output, pos, arr} = calculator(arr, phaseSetting[i % 5], modules[(i % 5) - 1])
      if (output) {
        val = output;
        modules[i % 5] = newVal
      } else {
        return val;
      }
    } else {
      newVal = calculator(arr, phaseSetting[0], modules[4])
      if (newVal) {
        val = newVal;
        modules[0] = newVal
      } else {
        return val;
      }
    }
    i++;
  }

  return val;
}

let getHighestSignal = function(signal) {
  let maxSignalPerm = []
  let maxSignal = -1;
  let phases = getPermutations();

  for (let i = 0 ; i < phases.length; i++) {
    let currPhase = phases[i];
    let val = amplifySignal(signal, 0, currPhase);

    if(val > maxSignal) {
      maxSignal = val;
      maxSignalPerm = phases[i]
    }
  }
  
  console.log(maxSignal, maxSignalPerm);
}


let signal1 = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0';
let signal2 = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10';
let signal3 = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0';



getHighestSignal(signal1);
//console.log(calculator(signal2, 5, 0))


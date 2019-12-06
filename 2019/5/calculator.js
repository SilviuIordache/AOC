const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  //input: fs.createReadStream('./input.txt'),
  input: fs.createReadStream('./2019/5/input.txt'),
  output: process.stdout,
  terminal: false
});

rl.on('line', function(line) {
  //console.log(calculator(line));
  calculator(line)
})


let calculator = function(code, input = 1) {
  let arr = code.split(',').map(function(item) {
      return parseInt(item, 10);
  })
  let pos = 0;
  while (arr[pos] != 99) {
    let currValue = arr[pos]
    let inst = getInstructionData(currValue);
    let { opcode, p1, p2, p3} = inst;

    val1 = arr[pos + 1]
    val2 = arr[pos + 2]
    dest = arr[pos + 3]
    arg1 = mval(p1, arr[pos + 1], arr);
    arg2 = mval(p2, arr[pos + 2], arr);

    switch(opcode) {
      case 1:
        arr[arr[pos + 3]] = arg1 + arg2;
        pos += 4;  
        break;
      case 2:
        arr[arr[pos + 3]] = arg1* arg2;
        pos += 4;  
        break;
      case 3:
        arr[arr[pos + 1]] = input;
        pos += 2;
        break;
      case 4:
        console.log(arg1)
        pos += 2;
        break;
      default:
        pos += 4;
        break;
    }

  }
}


let showArr = function(arr) {
  let smallArr = []
  for (let i = 0; i < 30; i++) {
    smallArr.push(arr[i]);
  }
  console.log(smallArr);
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
